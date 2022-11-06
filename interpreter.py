import token
import lexer
import parser

INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, MODULO, LPAREN, RPAREN, ASSIGN, SEMI, ID, LCURL, RCURL, EOF = (
        'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO', '(', ')', '=', ';', 'ID', '{', '}', 'EOF'
        )

class NodeVisitor(object):
    def visit(self, node):
        methodName = 'visit' + type(node).__name__
        visitor = getattr(self, methodName, self.genericVisit)
        return visitor(node)

    def genericVisit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

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

    def interpreter(self):
        tree = self.parser.parse()
        return self.visit(tree)

def main():
    while True:
        try:
            text = input('Rust Interpreter> ')
        except EOFError:
            break
        if not text:
            continue
        LEXER = lexer.Lexer(text)
        PARSER = parser.Parser(LEXER)
        INTERPRETER = Interpreter(PARSER)
        result = INTERPRETER.interpreter()
        print(result)

if __name__ == '__main__':
        main()