from Lexer import Lexer
from stackMachine import StackMachine
from syntax_parser import Syntax_Parser

if __name__ == '__main__':
    Lexer = Lexer()
    Lexer.get_term('test.txt')
    print('Tokens:', Lexer.list_tokens)
    try:
        Syntax_Parser = Syntax_Parser(Lexer.list_tokens)
        Tree = Syntax_Parser.S()
        print('Tree:\n', Tree)
        StackMachine = StackMachine(Tree.children)
        StackMachine.start()
    except BaseException as e:
        print('Syntax error' + str(e))
