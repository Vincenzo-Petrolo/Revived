# Models an assembly instruction
class Instruction(object):
    def __init__(self, instruction, operands) -> None:
        self.instruction = instruction
        self.operands = operands
    
    def getInstruction(self):
        return self.instruction
    
    def getOperands(self):
        return self.operands
    
    def __str__(self) -> str:
        string = f"\t{self.instruction}\t"

        for operand in self.operands:
            string += f"{operand},"
        
        string = string.removesuffix(',')
        string += '\n'

        return string


class Label(object):
    def __init__(self, label : str) -> None:
        self.label = label


    def getLabel(self):
        return self.label

    def __str__(self) -> str:
        return self.label + '\n'