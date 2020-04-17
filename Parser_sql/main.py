import sys

import astpretty
from antlr4 import FileStream
from antlr4.tree import Trees

from sqlast import parse
from sql_parser.sqlLexer import sqlLexer
from sql_parser.sqlParser import sqlParser, CommonTokenStream
from utils import *


def main():
    # input_stream = FileStream('./sql_stmt.sql')
    # lexer = sqlLexer(input_stream)
    # stream = CommonTokenStream(lexer)
    # parser = sqlParser(stream)
    # tree = parser.root()
    #
    # t = Trees.Trees.toStringTree(tree, parser.ruleNames)
    # print(t)

    ast_tree = parse(read_file('./sql_stmt.sql'))
    astpretty.pprint(ast_tree)

if __name__ == '__main__':
    main()
