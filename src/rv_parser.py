from rv_lexobj import Label, Instruction

class Parser(object):
    def __init__(self) -> None:
        # Contain a list of Labels & Instructions
        self.riscv_program = []
    
    def addRiscLine(self, line : Instruction | Label):
        if (line is not None):
            self.riscv_program.append(line)
    
    def __str__(self) -> str:
        string = ""

        for line in self.riscv_program:
            string += str(line)

        return string