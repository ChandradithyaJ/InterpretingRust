from enum import Enum

class ErrorCode(Enum):
    UNEXPECTED_TOKEN = 'Unexpected token'
    ID_NOT_FOUND     = 'Identifier not found'
    DUPLICATE_ID     = 'Duplicate id found'

class Error(Exception):
    def __init__(self, error_code=None, token=None, message=None):
        self.error_code = error_code
        self.token = token
        # add exception class name before the message
        self.message = f'{self.__class__.__name__}: {message}'

class LexerError(Error):
    pass

class ParserError(Error):
    pass

class SemanticError(Error):
    pass



INTEGER = 'INTEGER'
NUMBER = 'NUMBER'
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

FOR = 'for'
IF = 'if'
ELSEIF = 'else if'
ELSE = 'else'
LET = 'let'
WHILE = 'while'
PRINT = "println!"

EOF = 'EOF'

class Token(object):
    def __init__(self, type, value ,  line=None, column=None):
        # token type: INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN, MODULO, EOF
        self.type = type
        # value: +, -, *, /, %, None
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        """String representation of the class instance.
        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return 'Token({type}, {value} , position={line}:{column})'.format(
            type=self.type,
            value=repr(self.value),
            line=self.line,
            column=self.column)

    def __repr__(self):
        return self.__str__()
