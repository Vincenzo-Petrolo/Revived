# Models an assembly instruction
class Instruction(object):
    def __init__(self, instruction, operands) -> None:
        self.instruction = instruction
        self.operands = operands
    
    def getInstruction(self):
        return self.instruction
    
    def getOperands(self):
        return self.operands

class Label(object):
    def __init__(self, label) -> None:
        self.label = label
    

    def getLabel(self):
        return self.label
