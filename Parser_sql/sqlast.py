import astpretty

from antlr_ast.ast import (
    AliasNode,
    BaseNode as AstNode,  # used in other tests
    parse as parse_ast,
    process_tree,
    BaseNodeTransformer,
    Terminal,
)
from antlr_ast.inputstream import CaseTransformInputStream
from antlr_ast.marshalling import AstEncoder, get_decoder

from Parser_sql.sql_parser.sqlParser import sqlParser
from Parser_sql.sql_parser.sqlLexer import sqlLexer


class Grammar:
    @staticmethod
    def Lexer(arg):
        return sqlLexer(arg)

    @staticmethod
    def Parser(arg):
        return sqlParser(arg)


class RootQueryNode(AliasNode):
    _fields_spec = ['queries']

class QueryNode(AliasNode):
    _fields_spec = ['query_statements']

class FactoredStatementNode(AliasNode):
    _fields_spec = ['select_parts', 'operators']

class SelectNode(AliasNode):
    _fields_spec = ['columns', 'tables', 'where', 'group_by', 'having']

class ExprNode(AliasNode):
    _fields_spec = ['database_name', 'table_name', 'column_name', 'select_stmt', 'expr', 'literal_value']

class Transformer(BaseNodeTransformer):
    def visit_Expr(self, node):
        return ExprNode.from_spec(node)

    def visit_Root(self, node):
        return RootQueryNode.from_spec(node)

    def visit_Query_statements_list(self, node):
        return QueryNode.from_spec(node)

    def visit_Factored_select_stmt(self, node):
        return FactoredStatementNode.from_spec(node)

    def visit_Select_core(self, node):
        return SelectNode.from_spec(node)

    def visit_Terminal(self, terminal: Terminal) -> Terminal:
        return terminal.value


def parse(text, start="root", **kwargs):
    antlr_tree = parse_ast(
        Grammar, text, start, **kwargs
    )
    simple_tree = process_tree(antlr_tree, transformer_cls=Transformer)

    return simple_tree
