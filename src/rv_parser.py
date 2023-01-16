from rv_lexobj import Label, Instruction
from maps import regs_map, pseudo_map
import re

class Parser(object):
    def __init__(self) -> None:
        # Contain a list of Labels & Instructions
        self.riscv_program  =   []
        self.dlx_program    =   []
    
    def addRiscLine(self, line : Instruction | Label):
        if (line is not None):
            self.riscv_program.append(line)
            self.dlx_program.append(self.convert(line))
    
    def __str__(self) -> str:
        string = ""

        for line in self.riscv_program:
            string += str(line)

        return string
    
    def convert(self, rv_inst : Instruction | Label):
        # Label -> exit
        if (type(rv_inst) == Label):
            return Label(rv_inst.getLabel())

        dlx_inst = ""
        dlx_operands = []

        # Convert first the instruction
        if (rv_inst.getInstruction() in pseudo_map.keys()):
            # A pseudo instruction will take care of generating
            # also the converted operands
            dlx_inst, dlx_operands = self.convertPseudo(rv_inst)
        else:
            dlx_inst = rv_inst.getInstruction()
            # Convert the operands
            dlx_operands = self.convertOperands(rv_inst.getOperands())
        
        dlx_instruction = Instruction(dlx_inst, dlx_operands)

        return dlx_instruction
    
    def convertOperands(self, rv_operands : list):
        dlx_operands = []

        for operand in rv_operands:
            dlx_operand = operand
            if (str(operand).startswith('-') and str(operand).removeprefix('-').isdigit()):
                dlx_operands.append(f"#{dlx_operand}")
            elif (operand in regs_map.keys()):
                dlx_operands.append(regs_map[operand])
            elif (re.match(r"-*\d*\((\S*)\)", operand)):
                result = re.match(r"-*\d*\((\S*)\)", operand)
                reg    = result.group(1)
                dlx_operand = dlx_operand.replace(reg, regs_map[reg])
                dlx_operands.append(dlx_operand)
        
        return dlx_operands
    
    def convertPseudo(self, rv_inst : Instruction):
        dlx_op = ""
        dlx_operands = []

        if (rv_inst.getInstruction() in ["li", "mv"]):
            dlx_op = "addi"
            dlx_operands += self.convertOperands(rv_inst.getOperands())
            dlx_operands += ["#0"]
        elif (rv_inst.getInstruction() == "not"):
            dlx_op = pseudo_map[rv_inst.getInstruction()]
            dlx_operands += self.convertOperands(rv_inst.getOperands())
            dlx_operands += ["#-1"]
        elif (rv_inst.getInstruction() == "neg"):
            dlx_op = pseudo_map[rv_inst.getInstruction()]
            tmp_operands = self.convertOperands(rv_inst.getOperands())
            dlx_operands += [tmp_operands[0], "r0", tmp_operands[1]]
        elif (rv_inst.getInstruction() == "call"):
            dlx_op = pseudo_map[rv_inst.getInstruction()]
            dlx_operands += rv_inst.getOperands()
        
        return dlx_op, dlx_operands

    
    def writeDlxProgram(self, output_file):
        with open(output_file, "w") as fp:
            for instr in self.dlx_program:
                fp.write(str(instr))

