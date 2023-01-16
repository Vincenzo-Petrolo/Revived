from rv_lexobj import Label, Instruction
from maps import regs_map, pseudo_map
import re

class Parser(object):
    def __init__(self) -> None:
        # Contain a list of Labels & Instructions
        self.riscv_program  =   []
        self.dlx_program    =   []
        self.branch_delay_slot  = 2 # After a branch instruction place a nop
        self.datamem_size   = 2048 #Bytes
    
    def addRiscLine(self, line : Instruction | Label):
        if (line is not None):
            self.riscv_program.append(line)
            self.dlx_program += self.convert(line)
    
    def __str__(self) -> str:
        string = ""

        for line in self.riscv_program:
            string += str(line)

        return string
    
    def convert(self, rv_inst : Instruction | Label):
        # Label -> exit
        if (type(rv_inst) == Label):
            return [Label(rv_inst.getLabel().removeprefix('.'))]

        dlx_inst = ""
        dlx_operands = []

        if (rv_inst.getInstruction() in pseudo_map.keys()):
            # A pseudo instruction will take care of generating
            # also the converted operands
            dlx_instructions = self.convertPseudo(rv_inst)

            return dlx_instructions
        else:
            dlx_inst = rv_inst.getInstruction()
            # Convert the operands
            if (len(rv_inst.getOperands()) == 2 and rv_inst.getInstruction() not in ["lw", "sw"]):
                tmp_operands = self.convertOperands(rv_inst.getOperands())
                dlx_operands = [tmp_operands[0], tmp_operands[0], tmp_operands[1]]
            elif (rv_inst.getInstruction() == "sw"):
                dlx_operands = self.convertOperands(rv_inst.getOperands())
                dlx_operands.reverse()
            else:
                dlx_operands = self.convertOperands(rv_inst.getOperands())

        
        dlx_instruction = Instruction(dlx_inst, dlx_operands)

        return [dlx_instruction]
    
    def convertOperands(self, rv_operands : list):
        dlx_operands = []

        for operand in rv_operands:
            dlx_operand = operand
            if ((str(operand).startswith('-') and str(operand).removeprefix('-').isdigit()) or operand.isdigit()):
                dlx_operands.append(f"#{dlx_operand}")
            elif (operand in regs_map.keys()):
                dlx_operands.append(regs_map[operand])
            elif (re.match(r"-*\d*\((\S*)\)", operand)):
                result = re.match(r"-*\d*\((\S*)\)", operand)
                reg    = result.group(1)
                dlx_operand = dlx_operand.replace(reg, regs_map[reg])
                dlx_operands.append(dlx_operand)
            else:
                dlx_operands.append(dlx_operand.removeprefix('.'))
        
        return dlx_operands
    
    def convertPseudo(self, rv_inst : Instruction):
        dlx_op = ""
        dlx_operands = []
        dlx_instructions = []

        if (rv_inst.getInstruction() in ["li", "mv"]):
            dlx_op = "addi"
            dlx_operands += self.convertOperands(rv_inst.getOperands())
            dlx_operands += ["#0"]
            dlx_instructions.append(Instruction(dlx_op, dlx_operands))
        elif (rv_inst.getInstruction() == "not"):
            dlx_op = pseudo_map[rv_inst.getInstruction()]
            dlx_operands += self.convertOperands(rv_inst.getOperands())
            dlx_operands += ["#-1"]
            dlx_instructions.append(Instruction(dlx_op, dlx_operands))
        elif (rv_inst.getInstruction() == "neg"):
            dlx_op = pseudo_map[rv_inst.getInstruction()]
            tmp_operands = self.convertOperands(rv_inst.getOperands())
            dlx_operands += [tmp_operands[0], "r0", tmp_operands[1]]
            dlx_instructions.append(Instruction(dlx_op, dlx_operands))
        elif (rv_inst.getInstruction() == "call"):
            dlx_op = pseudo_map[rv_inst.getInstruction()]
            dlx_operands += rv_inst.getOperands()
            dlx_instructions.append(Instruction(dlx_op, dlx_operands))
        elif (rv_inst.getInstruction() == "jr"):
            dlx_op = pseudo_map[rv_inst.getInstruction()]
            dlx_instructions.append(Instruction(dlx_op, ["r31"]))
        elif (rv_inst.getInstruction() in ["beq", "bne", "blt", "bgt", "ble", "bge"]):
            dlx_instructions += self.convertBranch(rv_inst)
        
        return dlx_instructions
    
    def convertBranch(self, rv_inst : Instruction):
        # Use register r28 to store the result from the set
        set_op      = pseudo_map[rv_inst.getInstruction()]
        operands    = rv_inst.getOperands()
        set_inst    = Instruction(set_op, ["r28"] + self.convertOperands(operands[:-1]))
        br_inst     = Instruction("bnez", ["r28"] + self.convertOperands([operands[-1]]))

        unrolled_inst = [set_inst, br_inst]

        return unrolled_inst
    
    def initStackPointer(self):
        sp_init = self.datamem_size - 1
        dlx_inst = Instruction("addi", self.convertOperands(["sp", "r0", str(sp_init)]))

        self.dlx_program = [dlx_inst] + self.dlx_program
    
    def solveDataDependencies(self):
        # Solving only RAW because WAW and WAR can't happen (?)
        for i, instruction in enumerate(self.dlx_program):

            if (type(instruction) == Label or instruction.getInstruction() == "sw"):
                continue

            operands = instruction.getOperands()

            if (len(operands) == 0):
                continue

            next_instr = self.getNextInstructions(i, 3)
            
            for j in range(len(next_instr)):
                if (type(next_instr[j]) == Label):
                    continue

                if (self.checkRAW(operands[0], next_instr[j])):
                    self.insertNOPs(3-j, i+1)
                    break
    
    def checkRAW(self, operand, instruction : Instruction):

        if (instruction.getInstruction() == "sw"):
            read_operands = instruction.getOperands()
        else:
            read_operands = instruction.getOperands()[1:]

        for read_operand in read_operands:
            if (operand in read_operand):
                return True


        return False
    
    def getNextInstructions(self, where, n_instr):
        instructions = []

        next = self.dlx_program[where + 1:]

        for inst in next:
            if (len(instructions) == n_instr):
                break
            if (type(inst) != Label):
                instructions.append(inst)
        
        return instructions

            
    def insertNOPs(self, n_nops, where):
        for n in range(n_nops):
            self.dlx_program.insert(where, Instruction("nop",[]))
    
    def solveBranchDelaySlot(self):
        for i, line in enumerate(self.dlx_program):
            if (type(line) == Label):
                continue
            if (line.getInstruction() in ["j", "jr", "jal", "beqz", "bnez"]):
                self.insertNOPs(self.branch_delay_slot, i+1)
                
    
    def writeDlxProgram(self, output_file):
        # Before writing, correct the code
        self.initStackPointer()
        self.solveDataDependencies()
        self.solveBranchDelaySlot()
        with open(output_file, "w") as fp:
            for instr in self.dlx_program:
                fp.write(str(instr))

