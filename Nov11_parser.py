import lexer

INTEGER = 'INTEGER'
NUMBER = 'NUMBER'

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


class AST(object):
    pass


class BinOP(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Compound(AST):
    """ Represents a BEGIN ... END block """
    def __init__(self):
        self.children = []


class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Compare(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Var(AST):
    """The Var node is constructed out of the ID token"""
    def __init__(self, token):
        self.token = token
        self.value = token.value


class NoOp(AST):
    pass

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid Syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def program(self):
        """program:     compound_statement EOF"""
        node = self.compound_statement()
        return node


    def compound_statement(self):
        """compound_statement:  BEGIN statement_list END"""
        nodes = self.statement_list()

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root


    def statement_list(self):
        """
        statement_list : statement
                       | statement SEMI statement_list
        """
        node = self.statement()
        results = [node]

        while self.current_token.type != EOF:
            results.append(self.statement())

        return results

    def statement(self):
        """
        statement:      compound_statememt
                        | assignment_statement
                        | empty
        """
        if self.current_token.type == LET:
            node = self.assignment_statement()
        else:
            node = self.bool_expr()

        return node
        # more to be added (if, while)

    ################

    def assignment_statement(self):
        """
        assignment_statement:   variable ASSIGN expr
        """
        left = self.variable()
        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    ################

    def variable(self):
        """
        variable:   ID
        """
        node = Var(self.current_token)
        self.eat(LET)
        return node

    def empty(self):
        "empty production"
        return NoOp()

    def bool_expr(self):
        "bool_expr: expr comparision_operator expr"
        node = self.expr()

        while self.current_token.type in (EQ, NE, GT, LT, GE, LE):
            token = self.current_token
            self.eat(token.type)
            node = Compare(left=node, op=token, right=self.expr())
        return node

    def expr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER | LPAREN expr RPAREN
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOP(left=node, op=token, right=self.term())

        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in (MULTIPLY, DIVIDE, MODULO):
            token = self.current_token
            if token.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif token.type == DIVIDE:
                self.eat(DIVIDE)
            elif token.type == MODULO:
                self.eat(MODULO)
            node = BinOP(left=node, op=token, right=self.factor())

        return node

    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == NUMBER:
            self.eat(NUMBER)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            node = self.variable()
            return node

    def parse(self):
        node = self.program()
        while self.current_token.type != EOF:
            self.error()
        return node



def main():
    with open('testLexer.txt') as f:
        text = f.read()
    lex = lexer.Lexer(text)
    par = Parser(lex)
    result = par.parse()
    print(result)


if __name__ == '__main__':
    main()

