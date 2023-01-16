import re
from rv_lexobj import Label, Instruction

class Lexer(object):
    def __init__(self) -> None:
        pass

    def forward(self, line : str):
        tokens = self._parseLine(line)

        if (tokens != None):
            if (len(tokens) == 1):
                # Label
                return Label(tokens[0])
            elif (len(tokens) in [2, 3, 4]):
                # Other insturctions
                return Instruction(tokens[0], tokens[1:])
            else:
                raise Exception("Unknown instruction")


    def _parseLine(self, line : str):
        # Clean the line from junk
        line = line.strip(' ').strip('\t').strip('\n')

        if (line.startswith('.')):
            return None

        tokens = re.split("\t|,", line)

        return tokens
    