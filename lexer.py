import token

INTEGER = 'INTEGER'
NUMBER = 'NUMBER'

PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
MODULO = 'MODULO'

LPAREN = '('
RPAREN = ')'
LCURL = '{'
RCURL = '}'

ASSIGN = '='
SEMI = ';'
ID = 'ID'
COMMA = ','
DOT = '.'

FOR = 'FOR'
IF = 'IF'
ELSE = 'ELSE'
LET = 'LET'

EOF = 'EOF'

# identifiers: for, if, else if, else
RESERVED_KEYWORDS = {
    'for': token.Token(FOR, 'for'),
    'if': token.Token(IF, 'if'),
    'else': token.Token(ELSE, 'else'),
    'let': token.Token(LET, 'let'),
    #'let mut': token.Token('let mut', 'let mut'),
    #'in': token.Token('IN', 'in')
}

class Lexer(object):
    def __init__(self, text):
        # string input: "3 + 8"
        self.text = text
        # index to the text
        self.pos = 0
        # line of the text
        self.line = 1
        # current token
        self.currentToken = None
        self.currentChar = self.text[self.pos]

    def error(self):
        raise Exception('Invalid syntax')

    def advance(self):
        # advance the pos variable to go to the next char
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.currentChar = None
        else:
            self.currentChar = self.text[self.pos]

    def peek(self, n):
        peekPos = self.pos + n
        if peekPos > len(self.text) - 1:
            return None
        else:
            return self.text[peekPos]

    def skipWhiteSpace(self):
        # skip white spaces
        while self.currentChar is not None and self.currentChar.isspace():
            if self.currentChar == '\n':
                self.line += 1
            self.advance()

    def number(self):
        # return an integer read in from the input
        result = ''
        while self.currentChar is not None and self.currentChar.isdigit():
            result += self.currentChar
            self.advance()

        if self.currentChar == '.':
            result += self.currentChar
            self.advance()

            while self.currentChar is not None and self.currentChar.isdigit():
                result += self.currentChar
                self.advance()

            tok = token.Token('NUMBER', float(result))

        else:
            tok = token.Token('INTEGER', int(result))

        return tok

    def _id(self):
        # handles identifiers and reserved keywords
        result = ''
        while self.currentChar is not None and self.currentChar.isalnum():
            result += self.currentChar
            self.advance()

        tok = RESERVED_KEYWORDS.get(result, token.Token(ID, result))
        return tok

    def getNextToken(self):
        "Lexical Analyzer"
        "Breaks the input into tokens"

        while self.currentChar is not None:
            if self.currentChar.isspace():
                self.skipWhiteSpace()
                continue

            if self.currentChar.isdigit():
                return self.number()

            if self.currentChar.isalpha():
                return self._id()

            if self.currentChar == '+':
                self.advance()
                return token.Token(PLUS, '+')

            if self.currentChar == '-':
                self.advance()
                return token.Token(MINUS, '-')

            if self.currentChar == '*':
                self.advance()
                return token.Token(MULTIPLY, '*')

            if self.currentChar == '/':
                self.advance()
                return token.Token(DIVIDE, '/')

            if self.currentChar == '%':
                self.advance()
                return token.Token(MODULO, '%')

            if self.currentChar == '(':
                self.advance()
                return token.Token(LPAREN, '(')

            if self.currentChar == ')':
                self.advance()
                return token.Token(RPAREN, ')')

            if self.currentChar == '{':
                self.advance()
                return token.Token(LCURL, '{')

            if self.currentChar == '}':
                self.advance()
                return token.Token(RCURL, '}')

            if self.currentChar == '=':
                self.advance()
                return token.Token(ASSIGN, '=')

            if self.currentChar == ';':
                self.advance()
                return token.Token(SEMI, ';')

            if self.currentChar == ',':
                self.advance()
                return token.Token(COMMA, ',')

            self.error(
                message = "Invalid char {} at line {}".format(self.currentChar, self.line)
            )

        return token.Token(EOF, None)