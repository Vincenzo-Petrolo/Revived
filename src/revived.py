from rv_lexer import Lexer
from rv_parser import Parser
import getopt, sys

version = '0.0'

def print_help():
    print(f"Usage: python3 revived.py <options>")
    print(f"Available options:")
    print(f"\t--help(-h)\t\t: Show this help")
    print(f"\t--version(-v)\t\t: Show the version of the program")
    print(f"\t--input(-i)\t\t: Path to the RISC-V assembly file")
    print(f"\t--output(-o)\t\t: Name of the final generated DLX assembly")



def print_version():
    print(f"(R)andom (C)ircuit (G)raph (G)enerator v{version}")


if __name__ == "__main__":
    # Command parsing
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vho:", [   "help", 
                                                            "version",
                                                            "output=", 
                                                            "input="
                                                            ])
    except getopt.GetoptError as err:
        print(err)
        print_help()
        exit(2)

    output_filename = None
    input_filename = None

    for o,a in opts:
        if o in ['-o', '--output']:
            output_filename = a
        elif o in ['-i', '--input']:
            input_filename = a
        elif o in ['-h', '--help']:
            print_help()
            exit(0)
        elif o in ['-v', '--version']:
            print_version()
            exit(0)

    l = Lexer()
    p = Parser()

    if (input_filename is None):
        print_help()
        exit(0)
    
    if (output_filename is None):
        output_filename = "a.out"

    with open(input_filename, "r") as f:
        for line in f:
            obj = l.forward(line)
            p.addRiscLine(obj)
        
        p.writeDlxProgram(output_filename)
