# InterpretingRust
A python interpreter to interpret a subset of Rust
INTERPRETATION:
Interpretation lies at the opposite end (from compilation) of implementation methods. With this approach, programs are interpreted by another program called an interpreter, with no translation whatever.
The interpreter program acts as a software simulation of a machine whose fetch-execute cycle deals with high-level language program statements rather than machine instructions. This software simulation obviously provides a virtual machine for the language interpretation has the advantage of allowing easy implementation of many source-level debugging operations, because all run-time error messages can refer to source-level units. 
For example, if an array index is found to be out of range, the error message can easily indicate the source line and the name of the array. On the other hand, this method has the serious disadvantage that execution is 10 to 100 times slower than in compiled systems. The primary source of this slowness is the decoding of the high-level language statements, which are far more complex than machine language instructions (although there may be fewer statements than instructions in equivalent machine code). Furthermore, regardless of how many times a statement is executed, it must be decoded every time. Therefore, statement decoding, rather than the connection between the processor and memory, is the bottleneck of a pure interpreter.Another disadvantage of pure interpretation is that it often requires more space. In addition to the source program, the symbol table must be present during interpretation. Furthermore, the source program may be stored in a form designed for easy access and modification rather than one that provides for minimal size.Although some simple early languages of the 1960s (APL, SNOBOL, and LISP) were purely interpreted, by the 1980s, the approach was rarely used on high-level languages. However, in recent years, pure interpretation has made a significant comeback with some Web scripting languages, such as JavaScript and PHP, which are now widely used.
![image](https://user-images.githubusercontent.com/110807370/200530497-0226ab1a-d12c-4b49-8575-6f28cbc6aa1c.png) This iamge shows the breif graph of interpretaion process

INTERPRETER:
All high level languages need to be converted to machine code so that the computer can understand the program after taking the required inputs. The software by which the conversion of the high level instructions is performed line-by-line to machine level language, other than compiler and assembler, is known as INTERPRETER. If an error is found on any line, the execution stops till it is corrected.
This process of correcting errors is easier as it gives line-by-line error but the program takes more time to execute successfully. Interpreters were first used in 1952 to ease programming within the limitations of computers at the time. 
It translates source code into some efficient intermediate representation and immediately execute this.
Source programs are compiled ahead of time and stored as machine independent code, which is then linked at run-time and executed by an interpreter. An Interpreter is generally used in micro computer. It helps the programmer to find out the errors and to correct them before control moves to the next statement. 
Interpreter system performs the actions described by the high level program. For interpreted programs, the source code is needed to run the program every time. Interpreted programs run slower than the compiled programs. Self-Interpreter is a programming language interpreter which is written in a language which can interpret itself. 
For Example- BASIC interpreter written in BASIC. They are related to self-hosting compilers. Some languages have an elegant and self-interpreter such as Lisp and Prolog. Need of an Interpreter : The first and vital need of an interpreter is to translate source code from high-level language to machine language. However, for this purpose Compiler is also there to satisfy this condition. The compiler is a very powerful tool for developing programs in high-level language. However, there are several demerits associated with the compiler. 
If the source code is huge in size, then it might take hours to compile the source code, which will significantly increase the compilation duration. Here, Interpreter plays its role. They can cut this huge compilation duration. They are designed to translate single instruction at a time and execute them immediately.
![image](https://user-images.githubusercontent.com/110807370/200531762-f6f8d52a-9248-4b8b-9778-8d97ad07c55f.png)This image shows the breif graph of interpreter 



*Advantage and Disadvantage of Interpreter :

Advantage of interpreter is that it is executed line by line which helps users to find errors easily.

Disadvantage of interpreter is that it takes more time to execute successfully than compiler.





Applications of Interpreters :

*Each operator executed in a command language is usually an invocation of a complex routine, such as an editor or compiler so they are frequently used to command languages and glue languages.
*Virtualization is often used when the intended architecture is unavailable.
*Sand-boxing
*Self-modifying code can be easily implemented in an interpreted language.
*Emulator for running Computer software written for obsolete and unavailable hardware on more modern equipment.


*Some examples of programming languages that use interpreters are Python, Ruby, Perl, PHP and Matlab. Top Interpreters according to the computer languages –

Python- CPython, PyPy, Stackless Python, IronPython
Ruby- YARV, Ruby MRI (CRuby)
JAVA- HotSpot, OpenJ9, JRockIt
Kotlin- JariKo

LEXER

In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters (such as in a computer program or web page) into a sequence of lexical tokens (strings with an assigned and thus identified meaning). A program that performs lexical analysis may be termed a lexer, tokenizer, or scanner, although scanner is also a term for the first stage of a lexer. A lexer is generally combined with a parser, which together analyze the syntax of programming languages, web pages, and so forth.

*Applications of Lexer

A lexer forms the first phase of a compiler frontend in modern processing. Analysis generally occurs in one pass. In older languages such as ALGOL, the initial stage was instead line reconstruction, which performed unstropping and removed whitespace and comments (and had scannerless parsers, with no separate lexer). These steps are now done as part of the lexer.

Lexers and parsers are most often used for compilers, but can be used for other computer language tools, such as prettyprinters or linters. Lexing can be divided into two stages: the scanning, which segments the input string into syntactic units called lexemes and categorizes these into token classes; and the evaluating, which converts lexemes into processed values.

Lexers are generally quite simple, with most of the complexity deferred to the parser or semantic analysis phases, and can often be generated by a lexer generator, notably lex or derivatives. However, lexers can sometimes include some complexity, such as phrase structure processing to make input easier and simplify the parser, and may be written partly or fully by hand, either to support more features or for performance.

A lexeme is a sequence of characters in the source program that matches the pattern for a token and is identified by the lexical analyzer as an instance of that token.

Some authors term this a "token", using "token" interchangeably to represent the string being tokenized, and the token data structure resulting from putting this string through the tokenization process.

The word lexeme in computer science is defined differently than lexeme in linguistics. A lexeme in computer science roughly corresponds to a word in linguistics (not to be confused with a word in computer architecture), although in some cases it may be more similar to a morpheme. In some natural languages (for example, in English), the linguistic lexeme is similar to the lexeme in computer science, but this is generally not true (for example, in Chinese, it is highly non-trivial to find word boundaries due to the lack of word separators).

PARSER

*What is a parser
A parser is a compiler or interpreter component that breaks data into smaller elements for easy translation into another language. A parser takes input in the form of a sequence of tokens, interactive commands, or program instructions and breaks them up into parts that can be used by other components in programming.

A parser usually checks all data provided to ensure it is sufficient to build a data structure in the form of a parse tree or an abstract syntax tree.


In order for the code written in human-readable form to be understood by a machine, it must be converted into machine language. This task is usually performed by a translator (interpreter or compiler). The parser is commonly used as a component of the translator that organizes linear text in a structure that can be easily manipulated (parse tree). To do so, it follows a set of defined rules called “grammar”.

The overall process of parsing involves three stages:

1.Lexical Analysis: A lexical analyzer is used to produce tokens from a stream of input string characters, which are broken into small components to form meaningful expressions. A token is the smallest unit in a programming language that possesses some meaning (such as +, -, *, “function”, or “new” in JavaScript).

2.Syntactic Analysis: Checks whether the generated tokens form a meaningful expression. This makes use of a context-free grammar that defines algorithmic procedures for components. These work to form an expression and define the particular order in which tokens must be placed.

3.Semantic Parsing: The final parsing stage in which the meaning and implications of the validated expression are determined and necessary actions are taken.

A parser's main purpose is to determine if input data may be derived from the start symbol of the grammar. If yes, then in what ways can this input data be derived? This is achieved as follows:

****.Top-Down Parsing: Involves searching a parse tree to find the left-most derivations of an input stream by using a top-down expansion. Parsing begins with the start symbol which is transformed into the input symbol until all symbols are translated and a parse tree for an input string is constructed. Examples include LL parsers and recursive-descent parsers. Top-down parsing is also called predictive parsing or recursive parsing.

****.Bottom-Up Parsing: Involves rewriting the input back to the start symbol. It acts in reverse by tracing out the rightmost derivation of a string until the parse tree is constructed up to the start symbol This type of parsing is also known as shift-reduce parsing. One example is an LR parser.


TOKEN

A programming token is the basic component of source code. Characters are categorized as one of five classes of tokens that describe their functions (constants, identifiers, operators, reserved words, and separators) in accordance with the rules of the programming language.

*Types of Tokens

Identifiers (Identifiers are names given to different names given to entities such as constants, variables, structures, functions etc.)
Keywords (C has 32 reserved keywords)
Constants (Constants are like a variable, except that their value never changes during execution once defined)
Strings (The string can be defined as the one-dimensional array of characters terminated by a null (‘\0’).
Operators (C operators are symbols that are used to perform mathematical or logical manipulations like =,>=,+,/,* ….)
Special Symbols
