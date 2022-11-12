import lexer
import parser

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


class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):

    variables = dict()

    def __init__(self, parser):
        self.parser = parser

    def visit_BinOP(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIVIDE:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == MODULO:
            return self.visit(node.left) % self.visit(node.right)
        elif node.op.type == EQ:
            return self.visit(node.left) == self.visit(node.right)
        elif node.op.type == NE:
            return self.visit(node.left) != self.visit(node.right)
        elif node.op.type == GT:
            return self.visit(node.left) > self.visit(node.right)
        elif node.op.type == LT:
            return self.visit(node.left) < self.visit(node.right)
        elif node.op.type == GE:
            return self.visit(node.left) >= self.visit(node.right)
        elif node.op.type == LE:
            return self.visit(node.left) <= self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        var_name = node.left.value
        self.variables[var_name] = self.visit(node.right)

    def visit_Var(self, node):
        var_name = node.value
        val = self.variables.get(var_name)
        if val is None:
            raise NameError(repr(var_name))
        else:
            return val


    def visit_If(self, node):
        pass

    def visit_ElseIf(self, node):
        pass

    def visit_While(self, node):
        pass

    def visit_Compare(self, node):
        pass

    def visit_NoOp(self, node):
        pass

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)


def main():
    import sys

    with open('testInterpreter.txt') as f:
        text = f.read()
    lex = lexer.Lexer(text)
    par = parser.Parser(lex)
    inptr = Interpreter(par)
    result = inptr.interpret()
    print(inptr.variables)


if __name__ == '__main__':
        main()

