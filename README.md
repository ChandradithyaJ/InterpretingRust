InterpretingRust

A project to interpret a subset of Rust.

Rust is a multi-paradigm, general-purpose programming language. Rust emphasizes performance, type safety, and concurrency. Rust enforces memory safety — all references point to valid memory—without requiring the use of a garbage collector or reference counting present in other memory-safe languages

Constructs implemented:

  1.Arithematic Operations(Also kincludes the BODMAS rule)
  2.Operations on Strings and Charcters
  3.Assignment Operations for Strings, Characters, Integers, Floating Point
    Numbers and Boolean Values(True/false)
  4.If-else ladder
  5.While loop
  6.Comments

Four .py files make up the whole interpreter created - token.py, lexer.py, parser.py and interpreter.py. They are explained below in detail.

Lexer:
  CS21B059 Chandradithya
  CS21B033 Karthikeya 
  CS21B016 Dakshayni
  CS21B010 Jyoshna
  
  Input: Rust test file
  Output: The next token(number/identifier/keyword/...)
  
  A lexer breaks an input stream of characters into token for the parsers. 
  
  The lexer's most important function called the get_next_token() gives the next token of
  to the parser. The tokens are of predefined types given in the beginning of each file.
  If a given string of characters doesn't consist a predefined token, an error is thrown.
  This function checks the first character using the self.current_char attribute and uses 
  a self.peek(n) function to check for characters after that without advancing. Another
  function called self.advance() takes care of this. Based on the first character, and 
  a few more (as required), necessary function is called to read in a string or an
  integer or a floating point number or skip comments and whitespaces.

Parser:
  CS21B059 Chandradithya 
  CS21B037 Nandhavardhan
  CS21B033 Karthikeya 

  Input: Output of the Lexer is the input 
  Output: The AST(Abstract Syntax Tree)
  
  A parser takes tokens given by the lexer and constructs an Abstract Syntax Tree (AST),
  a parse tree or some kind of a hierarchial structure that checks for the right syntax
  of a language. The parser here constructs an AST.
  
  An AST class and other node classes (such as Var, BinOP and Number) are created which
  represent the different nodes and their types in the AST. Based on the BNF of the Rust
  programming language, each function checks for the required syntax by 'eating' it,
  i.e., the self.eat() function checks the token required and calls the get_next_token()
  method if it is right or otherwise, throws an error.
  
  For example, an assigment statement must have a variable on the LHS, an assignment 
  operator in the middle and an expression on the RHS. If any of these aren't present,
  an error is thrown, indicating that there is a mistake in the code.
  
  Just to make things clear, terms are separated by '+' or '-' operators and factors are
  the result from expressions inside parentheses, or variables or numbers separated by
  '*', '/' or '%' operators. All of these are evaluated in the expr() function.

Semantic analyzer:
  CS21B059 Chandradithya
  CS21B037 Nandhavardhan
  
  Input: AST
  Output: Dictionary of all the variables created mapped to their values.
  
  A semantic analyzer uses the syntax tree to check whether the program is semantically
  consistent with the language or not.
  
  A NodeVisitor class is created which takes objects of a class, given by the parser, and
  invokes a visit_{class name} method which visits the node (the object) and evaluates
  it and stores the value in a dictonary, which is then printed as the output to show
  all the variables created and the values (integers, floating-point numbers, characters,
  or strings) mapped to them.
  
  For example, if the node (object) is a variable, it checks whether the variable exists
  or not, and if it doesn't exist, it throws an error. If the node is the assignment 
  operator, the value on the RHS is assigned to the variable on the LHS, as said, if it
  exists. Similarly, the visit_BinOP function takes the operator (==, <=, +, and more)
  and calculates the value by operating on the LHS (node.left) and RHS (node.right).

ReadMe File and BNF compilation:
  CS21B026 Karthik Prasad S
  CS21B059 Chandradithya
  CS21B037 Nandhavardhan
  
 Error Messaging:
  CS21B033 Karthikeya

