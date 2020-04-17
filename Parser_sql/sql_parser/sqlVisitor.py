# Generated from C:/Work/DTask/Pars\sql.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sqlParser import sqlParser
else:
    from sqlParser import sqlParser

# This class defines a complete generic visitor for a parse tree produced by sqlParser.

class sqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by sqlParser#root.
    def visitRoot(self, ctx:sqlParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#query_statements_list.
    def visitQuery_statements_list(self, ctx:sqlParser.Query_statements_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#compound_select.
    def visitCompound_select(self, ctx:sqlParser.Compound_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#factored_select.
    def visitFactored_select(self, ctx:sqlParser.Factored_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#simple_select.
    def visitSimple_select(self, ctx:sqlParser.Simple_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#general_select.
    def visitGeneral_select(self, ctx:sqlParser.General_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#vacuum_statement.
    def visitVacuum_statement(self, ctx:sqlParser.Vacuum_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#compound_select_stmt.
    def visitCompound_select_stmt(self, ctx:sqlParser.Compound_select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#factored_select_stmt.
    def visitFactored_select_stmt(self, ctx:sqlParser.Factored_select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#simple_select_stmt.
    def visitSimple_select_stmt(self, ctx:sqlParser.Simple_select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#select_stmt.
    def visitSelect_stmt(self, ctx:sqlParser.Select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#select_or_values.
    def visitSelect_or_values(self, ctx:sqlParser.Select_or_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#vacuum_stmt.
    def visitVacuum_stmt(self, ctx:sqlParser.Vacuum_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#expr.
    def visitExpr(self, ctx:sqlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#with_clause.
    def visitWith_clause(self, ctx:sqlParser.With_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#common_table_expression.
    def visitCommon_table_expression(self, ctx:sqlParser.Common_table_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#ordering_term.
    def visitOrdering_term(self, ctx:sqlParser.Ordering_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#result_column.
    def visitResult_column(self, ctx:sqlParser.Result_columnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#table_or_subquery.
    def visitTable_or_subquery(self, ctx:sqlParser.Table_or_subqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#join_clause.
    def visitJoin_clause(self, ctx:sqlParser.Join_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#join_operator.
    def visitJoin_operator(self, ctx:sqlParser.Join_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#join_constraint.
    def visitJoin_constraint(self, ctx:sqlParser.Join_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#select_core.
    def visitSelect_core(self, ctx:sqlParser.Select_coreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#compound_operator.
    def visitCompound_operator(self, ctx:sqlParser.Compound_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#signed_number.
    def visitSigned_number(self, ctx:sqlParser.Signed_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#literal_value.
    def visitLiteral_value(self, ctx:sqlParser.Literal_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#unary_operator.
    def visitUnary_operator(self, ctx:sqlParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#column_alias.
    def visitColumn_alias(self, ctx:sqlParser.Column_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#keyword.
    def visitKeyword(self, ctx:sqlParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#name.
    def visitName(self, ctx:sqlParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#database_name.
    def visitDatabase_name(self, ctx:sqlParser.Database_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#schema_name.
    def visitSchema_name(self, ctx:sqlParser.Schema_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#table_function_name.
    def visitTable_function_name(self, ctx:sqlParser.Table_function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#table_name.
    def visitTable_name(self, ctx:sqlParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#column_name.
    def visitColumn_name(self, ctx:sqlParser.Column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#collation_name.
    def visitCollation_name(self, ctx:sqlParser.Collation_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#index_name.
    def visitIndex_name(self, ctx:sqlParser.Index_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#table_alias.
    def visitTable_alias(self, ctx:sqlParser.Table_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#any_name.
    def visitAny_name(self, ctx:sqlParser.Any_nameContext):
        return self.visitChildren(ctx)



del sqlParser