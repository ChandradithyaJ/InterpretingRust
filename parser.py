import token
import lexer

INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, MODULO, LPAREN, RPAREN, ASSIGN, SEMI, ID, LCURL, RCURL, EOF = (
        'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO', '(', ')', '=', ';', 'ID', '{', '}', 'EOF'
        )

class AST(object):
    pass

class Compound(AST):
    # contains all the statement nodes in its children varaibles
    def __init__(self):
        self.children = []

class Assign(AST):
    # assignment statements
    # left node is the variable and the right node is the node returned by the expr parser method
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Var(AST):
    # holds a variable
    def __init__(self, token):
        self.token = token
        self.value = token.value

class NoOp(AST):
    # empty statement
    pass

class binOP(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.currentToken = self.lexer.getNextToken()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, tokenType):
        if self.currentToken.type == tokenType:
            self.currentToken = self.lexer.getNextToken()
        else:
            self.error()

    def factor(self):
        token = self.currentToken
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            node = self.variable()
            return node

    def term(self):
        node = self.factor()
        while self.currentToken.type in (MULTIPLY, DIVIDE, MODULO):
            token = self.currentToken
            if token.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif token.type == DIVIDE:
                self.eat(DIVIDE)
            elif token.type == MODULO:
                self.eat(MODULO)
            node = binOP(left = node, op = token, right = self.factor())

        return node

    def expr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER | LPAREN expr RPAREN
        """
        node = self.term()

        while self.currentToken.type in (PLUS, MINUS):
            token = self.currentToken
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = binOP(left=node, op=token, right=self.term())

        return node

    def program(self):
        """Program Statement: compound_statement endOfProgram"""
        node = self.compoundStatement()
        return node

    def compoundStatement(self):
        """
        compound statement = { statement_list }
        """
        self.eat(LCURL)
        nodes = self.statementList()
        self.eat(RCURL)

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root

    def statementList(self):
        """
        statement_list : statement
                       | statement SEMI statement_list
        """
        node = self.statement()

        results = [node]
        while self.currentToken.type == SEMI:
            self.eat(SEMI)
            results.append(self.statement())

        if self.currentToken.type == ID:
            self.error()

        return results

    def statement(self):
        """
            statement : compound_statement
                      | assignment_statement
                      | empty
            """

        if self.currentToken.type == LCURL:
            node = self.compoundStatement()
        elif self.currentToken.type == ID:
            node = self.assignmentStatement
        else:
            node = self.empty()

        return node

    def assignmentStatement(self):
        """
        variable ASSIGN expr
        """
        left = self.variable()
        token = self.currentToken
        self.eat(ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def variable(self):
        # variable: ID
        node = Var(self.currentToken)
        self.eat(ID)
        return node

    def empty(self):
        return NoOp()

    def parse(self):
        node = self.program()
        if self.currentToken.type != EOF:
            self.error()
        return node