# Calculator for Rust inputs
# Addition, Subtraction, Multiplication, Division and Modulo operation
INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, MODULO, LPAREN, RPAREN, EOF = (
        'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO', '(', ')', 'EOF'
        )

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
        return 'Token({type}, {value})'.format(type = self.type, value = repr(self.value))

    def __repr__(self):
        return self.__str__()

class Lexer(object):
    def __init__(self, text):
        # string input: "3 + 8"
        self.text = text
        # index to the text
        self.pos = 0
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

    def skipWhiteSpace(self):
        # skip white spaces
        while self.currentChar is not None and self.currentChar.isspace():
            self.advance()

    def integer(self):
        # return an integer read in from the input
        result = ''
        while self.currentChar is not None and self.currentChar.isdigit():
            result += self.currentChar
            self.advance()

        return int(result)

    def getNextToken(self):
        "Lexical Analyzer"
        "Breaks the input into tokens"

        while self.currentChar is not None:
            if self.currentChar.isspace():
                self.skipWhiteSpace()
                continue

            if self.currentChar.isdigit():
                return Token(INTEGER, self.integer())

            if self.currentChar == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.currentChar == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.currentChar == '*':
                self.advance()
                return Token(MULTIPLY, '*')

            if self.currentChar == '/':
                self.advance()
                return Token(DIVIDE, '/')

            if self.currentChar == '%':
                self.advance()
                return Token(MODULO, '%')

            if self.currentChar == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.currentChar == ')':
                self.advance()
                return Token(RPAREN, ')')

            self.error()

        return Token(EOF, None)

class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.currentToken = self.lexer.getNextToken()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, tokenType):
        # compares the current token with the expected one
        # and if they match, it 'eats' the token
        # and assigns the next token to the currentToken variable
        # if not, it throws an error

        if self.currentToken.type == tokenType:
            self.currentToken = self.lexer.getNextToken()
        else:
            self.error()

    def factor(self):
        """factor : INTEGER | LPAREN expr RPAREN"""
        token = self.currentToken
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result

    def term(self):
        # to take care of operator precedence we group the terms
        # which have a * or / operator

        result = self.factor()
        while self.currentToken.type in (MULTIPLY, DIVIDE, MODULO):
            token = self.currentToken
            if token.type == MULTIPLY:
                self.eat(MULTIPLY)
                result = result * self.factor()
            elif token.type == DIVIDE:
                self.eat(DIVIDE)
                result = result / self.factor()
            elif token.type == MODULO:
                self.eat(MODULO)
                result = result % self.factor()

        return result

    def expr(self):
        # Reads and parses the arithmetic expression

        result = self.term()
        while self.currentToken.type in (PLUS, MINUS):
            token = self.currentToken
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        return result

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
        main()