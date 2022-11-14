import token
from enum import Enum


class ErrorCode(Enum):
    UNEXPECTED_TOKEN = 'Unexpected token'
    ID_NOT_FOUND = 'Identifier not found'
    DUPLICATE_ID = 'Duplicate id found'


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
SLASH = '/'
DSLASH = '//'

FOR = 'for'
IF = 'if'
ELSEIF = 'else if'
ELSE = 'else'
LETMUT = 'let mut'
WHILE = 'while'

FN = 'fn'
MAIN = 'main'
EOF = 'EOF'

# identifiers: for, if, else if, else, while
RESERVED_KEYWORDS = {
    'for': token.Token(FOR, 'for'),
    'if': token.Token(IF, 'if'),
    'else if': token.Token(ELSEIF, 'else if'),
    'else': token.Token(ELSE, 'else'),
    'while': token.Token(WHILE, 'while'),
    'let mut': token.Token(LETMUT, 'let mut'),
    'fn': token.Token(FN, 'fn'),
    'main': token.Token(MAIN, 'main')
}


class Lexer(object):
    def __init__(self, text):
        # string input: "3 + 8"
        self.text = text
        # index to the text
        self.pos = 0
        # line of the text
        self.line = 1
        # column of the text
        self.column = 1
        # current token
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        s = "Lexer error on '{lexeme}' line: {line} column: {column}".format(
            lexeme=self.current_char,
            line=self.line,
            column=self.column,
            )
        raise LexerError(message=s)

    def advance(self):
        # advance the pos variable to go to the next char
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
            self.column += 1

    def peek(self, n):
        peek_pos = self.pos + n
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def skip_white_space(self):
        # skip white spaces
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == '\n':
                self.line += 1
            self.advance()

    def skip_comments(self):
        if self.current_char == '/' and self.peek(1) == '/':
            self.advance()
            self.advance()
            while self.current_char != '\n':
                self.advance()
            self.advance()

        # skip multi-line comments
        # Ha! Rust doesn't have a different symbol for multi-line comments

    def number(self):
        # return an integer or a float read in from the input
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()

            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()

            tok = token.Token('NUMBER', float(result))

        else:
            tok = token.Token('INTEGER', int(result))

        return tok

    def string(self):
        # returns a string read in from the input
        result = ''
        self.advance()
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()

        tok = token.Token('STR', result)
        return tok

    def _id(self):
        # handles identifiers and reserved keywords
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()

        if self.current_char == ' ' and self.peek(1) == 'i' and self.peek(2) == 'f' and self.peek(3) == ' ':
            self.advance()
            self.advance()
            self.advance()
            self.advance()
            return token.Token(ELSEIF, 'else if')

        if self.current_char == ' ' and self.peek(1) == 'm' and self.peek(2) == 'u' and self.peek(3) == 't' and self.peek(4) == ' ':
            self.advance()
            self.advance()
            self.advance()
            self.advance()
            self.advance()
            return token.Token(LETMUT, 'let mut')

        tok = RESERVED_KEYWORDS.get(result, token.Token(ID, result))
        return tok

    def get_next_token(self):
        """Lexical Analyzer"""
        """Breaks the input into tokens"""

        while self.current_char is not None:

            if self.current_char == '/' and self.peek(1) == '/':
                self.skip_comments()
                continue

            if self.current_char.isspace():
                self.skip_white_space()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == '"':
                return self.string()

            if self.current_char.isalpha():
                return self._id()

            if self.current_char == '+':
                self.advance()
                return token.Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return token.Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return token.Token(MULTIPLY, '*')

            if self.current_char == '/' and self.peek(1) != '/':
                self.advance()
                return token.Token(DIVIDE, '/')

            if self.current_char == '%':
                self.advance()
                return token.Token(MODULO, '%')

            if self.current_char == '(':
                self.advance()
                return token.Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return token.Token(RPAREN, ')')

            if self.current_char == '{':
                self.advance()
                return token.Token(LCURL, '{')

            if self.current_char == '}':
                self.advance()
                return token.Token(RCURL, '}')

            if self.current_char == '=' and self.peek(1) != '=':
                self.advance()
                return token.Token(ASSIGN, '=')

            if self.current_char == '=' and self.peek(1) == '=':
                self.advance()
                self.advance()
                return token.Token(EQ, '==')

            if self.current_char == '!' and self.peek(1) == '=':
                self.advance()
                self.advance()
                return token.Token(NE, '!=')

            if self.current_char == '<' and self.peek(1) == '=':
                self.advance()
                self.advance()
                return token.Token(LE, '<=')

            if self.current_char == '>' and self.peek(1) == '=':
                self.advance()
                self.advance()
                return token.Token(GE, '>=')

            if self.current_char == '>' and self.peek(1) != '=':
                self.advance()
                return token.Token(GT, '>')

            if self.current_char == '<' and self.peek(1) != '=':
                self.advance()
                return token.Token(LT, '<')

            if self.current_char == ';':
                self.advance()
                return token.Token(SEMI, ';')

            if self.current_char == ',':
                self.advance()
                return token.Token(COMMA, ',')

            if self.current_char == 'i' and self.peek(1) == 'f' and self.peek(2) == ' ':
                self.advance()
                self.advance()
                self.advance()
                return token.Token(IF, 'if')

            if self.current_char == 'e' and self.peek(1) == 'l' and self.peek(2) == 's' and self.peek(3) == 'e' and self.peek(4) == ' ' and self.peek(5) == 'i' and self.peek(6) == 'f' and self.peek(7) == ' ':
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                return token.Token(ELSEIF, 'else if')

            if self.current_char == 'e' and self.peek(1) == 'l' and self.peek(2) == 's' and self.peek(3) == 'e' and self.peek(5) != 'i':
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                return token.Token(ELSE, 'else')

            if self.current_char == 'w' and self.peek(1) == 'h' and self.peek(2) == 'i' and self.peek(3) == 'l' and self.peek(4) == 'e' and self.peek(5) == ' ':
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                return token.Token(WHILE, 'while')

            if self.current_char == chr(26):
                return token.Token(EOF, 'EOF')

            self.error(
                message="Invalid char {} at line {}".format(self.current_char, self.line)
            )

        return token.Token(EOF, None)
