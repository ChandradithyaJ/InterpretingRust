INTEGER = 'INTEGER'
NUMBER = 'NUMBER'
STR = 'STR'
TRUE = 'true'
FALSE = 'false'

PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
MODULO = 'MODULO'

EQ = '=='
NE = '!='
GT = '>'
LT = '<'
GE = '>='
LE = '<='

LPAREN = '('
RPAREN = ')'
LCURL = '{'
RCURL = '}'

ASSIGN = '='
SEMI = ';'
ID = 'ID'
COMMA = ','
DOT = '.'
QUO = '"'

FOR = 'for'
IF = 'if'
ELSEIF = 'else if'
ELSE = 'else'
LETMUT = 'let mut'
WHILE = 'while'

FN = 'fn'
MAIN = 'main'
EOF = 'EOF'


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN, MODULO, EOF
        self.type = type
        # value: +, -, *, /, %, None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()
