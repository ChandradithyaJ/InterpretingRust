import token
import lexer
import parser

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

class NodeVisitor(object):
    def visit(self, node):
        methodName = 'visit' + type(node).__name__
        visitor = getattr(self, methodName, self.genericVisit)
        return visitor(node)

    def genericVisit(self, node):
        raise Exception('No visit{} method'.format(type(node).__name__))

class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visitbinOP(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIVIDE:
            return self.visit(node.left) / self.visit(node.right)

    def visitNum(self, node):
        return node.value

    def visitCompound(self, node):
        for child in node.children:
            self.visit(child)

    def visitNoOp(self):
        pass

    def visitAssign(self, node):
        varName = node.left.value
        self.GLOBAL_SCOPE[varName] = self.visit(node.right)

    def visitVar(self, node):
        varName = node.value
        val = self.GLOBAL_SCOPE.get(varName)
        if val is None:
            raise NameError(repr(varName))
        else:
            return val

    def visitType(self, node):
        pass

    def visitVarDecl(self, node):
        pass

    def visitProgram(self, node):
        self.visit(node.block)

    def visitBlock(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compoundStatement)

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''
        return self.visit(tree)


def main():
    import sys
    text = input('Rust Interpreter> ')

    LEXER = lexer.Lexer(text)
    PARSER = parser.Parser(LEXER)
    INTERPRETER = Interpreter(PARSER)
    result = INTERPRETER.interpret()

    for k, v in sorted(INTERPRETER.GLOBAL_SCOPE.items()):
        print('{} = {}'.format(k, v))

if __name__ == '__main__':
        main()