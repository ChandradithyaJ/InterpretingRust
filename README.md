InterpretingRust
A project to interpret a subset of Rust.
Rust is a multi-paradigm, general-purpose programming language. Rust emphasizes performance, type safety, and concurrency. Rust enforces memory safety—that is, that all references point to valid memory—without requiring the use of a garbage collector or reference counting present in other memory-safe languages

Update!
We're done with our basic coding stuff, so let's go to the testing!
Every file is tested using test_*.py

The whole interpter the rust test case as an input 


What is an interpreter?
In computer science, an interpreter is a computer program that directly executes instructions written in a programming or scripting language, without requiring them previously to have been compiled into a machine language program.

What is the work of a lexer??
The lexical analyzer (or lexer) breaks up the input text stream into lexemes and returns a token object for each one.

What is the work of a parser?
A parser is a program that is part of the compiler, and parsing is part of the compiling process. Parsing happens during the analysis stage of compilation. In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it.(We are using Recursive descent parsing)

What is recursive descent parsing?
In computer science, a recursive descent parser is a kind of top-down parser built from a set of mutually recursive procedures where each such procedure implements one of the nonterminals of the grammar. Thus the structure of the resulting program closely mirrors that of the grammar it recognizes.

What is the work of Semantic analyser??
It uses syntax tree and symbol table to check whether the given program is semantically consistent with language definition. It gathers type information and stores it in either syntax tree or symbol table. This type information is subsequently used by compiler during intermediate-code generation.

In this program we are using lexer to make Abstract Syntax Tree 

Constructs impleted:
1.Arithematic Operations(Also kincludes the BODMAS rule)
2.Operations on Strings and Charcters
3.Assignment Operations for Strings,Characters,Integers,Floatinf=g Poinrt Numbers,Boolean Values(True/false)
4.If else  ladder
5.While loop
6.Comments

Lexer
Chandradithya,Karthikeya,Dakshayni,Jyoshna
Input: Rust test file

Output: The next token(number/identifier/keyword/...)

Parser
Chandraditya,Karthikeya,Nandhavardhan
Input: Output of the Lexer is the input 

Output: The AST(Abstract Syntax Tree)

Semantic analyser
Nandhavardhan,Chandradithya
Input: AST

ReadMe File and BNF compilation
Karthik Prasad S
Input:

KEYWORDS:

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



RESERVED KEYWORDS 
'for': token.Token(FOR, 'for'),
'if': token.Token(IF, 'if'),
'else if': token.Token(ELSEIF, 'else if'),
'else': token.Token(ELSE, 'else'),
'while': token.Token(WHILE, 'while'),
'let mut': token.Token(LETMUT, 'let mut'),
'fn': token.Token(FN, 'fn'),
'main': token.Token(MAIN, 'main')
