import lexer

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
LET = 'let'
WHILE = 'while'

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


class If(AST):
    def __init__(self, condition, body, elseif_body, else_body):
        self.condition = condition
        self.body = body
        self.elseif_body = elseif_body
        self.else_body = else_body


class ElseIf(AST):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class While(AST):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


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

        while self.current_token.type != EOF and self.current_token.type != RCURL:
            results.append(self.statement())

        return results

    def statement(self):
        """
        statement:      compound_statement
                        | assignment_statement
                        | empty
        """
        if self.current_token.type == LET:
            node = self.assignment_statement()
        elif self.current_token.type == IF:
            node = self.if_statement()
        elif self.current_token.type == WHILE:
            node = self.while_statement()
        else:
            node = self.conditional_statement()

        return node

    ################

    def assignment_statement(self):
        """
        assignment_statement:   variable ASSIGN expr
        """
        left = self.variable()
        self.eat(ID)
        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()
        self.eat(SEMI)
        node = Assign(left=left, op=token, right=right)
        return node

    ################

    def if_statement(self):
        """
        if_statement:       expr comparison_operator expr { statement_list } (else if* | else | empty)
        """
        self.eat(IF)
        condition = self.conditional_statement()
        self.eat(LCURL)
        body = self.statement_list()
        self.eat(RCURL)
        elseif_body = self.empty()
        else_body = self.empty()

        elseifs = []
        while self.current_token.type == ELSEIF:
            self.eat(ELSEIF)
            elseif_condition = self.conditional_statement()
            self.eat(LCURL)
            elseif_body = self.statement_list()
            elseif_node = ElseIf(elseif_condition, elseif_body)
            elseifs.append(elseif_node)
            self.eat(RCURL)
        if self.current_token.type == ELSE:
            self.eat(ELSE)
            self.eat(LCURL)
            else_body = self.statement_list()
            self.eat(RCURL)
        node = If(condition=condition, body=body, elseif_body=elseifs, else_body=else_body)
        return node

    ################

    def while_statement(self):
        self.eat(WHILE)
        condition = self.conditional_statement()
        self.eat(LCURL)
        body = self.statement_list()
        self.eat(RCURL)
        node = While(condition=condition, body=body)
        return node

    ################

    def variable(self):
        """
        variable:   ID
        """
        self.eat(LET)
        node = Var(self.current_token)
        return node

    def empty(self):
        """empty production"""
        return NoOp()

    def conditional_statement(self):
        """"conditional_statement: expr comparison_operator expr"""
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
        elif token.type == STR:
            self.eat(STR)
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

