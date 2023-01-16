from rv_lexer import Lexer
from rv_parser import Parser
from rv_lexobj import Instruction, Label

if __name__ == "__main__":
    l = Lexer()
    p = Parser()

    with open("riscv_asm/simple.s", "r") as f:
        for line in f:
            obj = l.forward(line)
            p.addRiscLine(obj)
        
        print(p)
