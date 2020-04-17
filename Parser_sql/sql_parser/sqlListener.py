# Generated from C:/Work/DTask/Pars\sql.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sqlParser import sqlParser
else:
    from sqlParser import sqlParser

# This class defines a complete listener for a parse tree produced by sqlParser.
class sqlListener(ParseTreeListener):

    # Enter a parse tree produced by sqlParser#root.
    def enterRoot(self, ctx:sqlParser.RootContext):
        pass

    # Exit a parse tree produced by sqlParser#root.
    def exitRoot(self, ctx:sqlParser.RootContext):
        pass


    # Enter a parse tree produced by sqlParser#query_statements_list.
    def enterQuery_statements_list(self, ctx:sqlParser.Query_statements_listContext):
        pass

    # Exit a parse tree produced by sqlParser#query_statements_list.
    def exitQuery_statements_list(self, ctx:sqlParser.Query_statements_listContext):
        pass


    # Enter a parse tree produced by sqlParser#compound_select.
    def enterCompound_select(self, ctx:sqlParser.Compound_selectContext):
        pass

    # Exit a parse tree produced by sqlParser#compound_select.
    def exitCompound_select(self, ctx:sqlParser.Compound_selectContext):
        pass


    # Enter a parse tree produced by sqlParser#factored_select.
    def enterFactored_select(self, ctx:sqlParser.Factored_selectContext):
        pass

    # Exit a parse tree produced by sqlParser#factored_select.
    def exitFactored_select(self, ctx:sqlParser.Factored_selectContext):
        pass


    # Enter a parse tree produced by sqlParser#simple_select.
    def enterSimple_select(self, ctx:sqlParser.Simple_selectContext):
        pass

    # Exit a parse tree produced by sqlParser#simple_select.
    def exitSimple_select(self, ctx:sqlParser.Simple_selectContext):
        pass


    # Enter a parse tree produced by sqlParser#general_select.
    def enterGeneral_select(self, ctx:sqlParser.General_selectContext):
        pass

    # Exit a parse tree produced by sqlParser#general_select.
    def exitGeneral_select(self, ctx:sqlParser.General_selectContext):
        pass


    # Enter a parse tree produced by sqlParser#vacuum_statement.
    def enterVacuum_statement(self, ctx:sqlParser.Vacuum_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#vacuum_statement.
    def exitVacuum_statement(self, ctx:sqlParser.Vacuum_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#compound_select_stmt.
    def enterCompound_select_stmt(self, ctx:sqlParser.Compound_select_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#compound_select_stmt.
    def exitCompound_select_stmt(self, ctx:sqlParser.Compound_select_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#factored_select_stmt.
    def enterFactored_select_stmt(self, ctx:sqlParser.Factored_select_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#factored_select_stmt.
    def exitFactored_select_stmt(self, ctx:sqlParser.Factored_select_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#simple_select_stmt.
    def enterSimple_select_stmt(self, ctx:sqlParser.Simple_select_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#simple_select_stmt.
    def exitSimple_select_stmt(self, ctx:sqlParser.Simple_select_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#select_stmt.
    def enterSelect_stmt(self, ctx:sqlParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#select_stmt.
    def exitSelect_stmt(self, ctx:sqlParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#select_or_values.
    def enterSelect_or_values(self, ctx:sqlParser.Select_or_valuesContext):
        pass

    # Exit a parse tree produced by sqlParser#select_or_values.
    def exitSelect_or_values(self, ctx:sqlParser.Select_or_valuesContext):
        pass


    # Enter a parse tree produced by sqlParser#vacuum_stmt.
    def enterVacuum_stmt(self, ctx:sqlParser.Vacuum_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#vacuum_stmt.
    def exitVacuum_stmt(self, ctx:sqlParser.Vacuum_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#expr.
    def enterExpr(self, ctx:sqlParser.ExprContext):
        pass

    # Exit a parse tree produced by sqlParser#expr.
    def exitExpr(self, ctx:sqlParser.ExprContext):
        pass


    # Enter a parse tree produced by sqlParser#with_clause.
    def enterWith_clause(self, ctx:sqlParser.With_clauseContext):
        pass

    # Exit a parse tree produced by sqlParser#with_clause.
    def exitWith_clause(self, ctx:sqlParser.With_clauseContext):
        pass


    # Enter a parse tree produced by sqlParser#common_table_expression.
    def enterCommon_table_expression(self, ctx:sqlParser.Common_table_expressionContext):
        pass

    # Exit a parse tree produced by sqlParser#common_table_expression.
    def exitCommon_table_expression(self, ctx:sqlParser.Common_table_expressionContext):
        pass


    # Enter a parse tree produced by sqlParser#ordering_term.
    def enterOrdering_term(self, ctx:sqlParser.Ordering_termContext):
        pass

    # Exit a parse tree produced by sqlParser#ordering_term.
    def exitOrdering_term(self, ctx:sqlParser.Ordering_termContext):
        pass


    # Enter a parse tree produced by sqlParser#result_column.
    def enterResult_column(self, ctx:sqlParser.Result_columnContext):
        pass

    # Exit a parse tree produced by sqlParser#result_column.
    def exitResult_column(self, ctx:sqlParser.Result_columnContext):
        pass


    # Enter a parse tree produced by sqlParser#table_or_subquery.
    def enterTable_or_subquery(self, ctx:sqlParser.Table_or_subqueryContext):
        pass

    # Exit a parse tree produced by sqlParser#table_or_subquery.
    def exitTable_or_subquery(self, ctx:sqlParser.Table_or_subqueryContext):
        pass


    # Enter a parse tree produced by sqlParser#join_clause.
    def enterJoin_clause(self, ctx:sqlParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by sqlParser#join_clause.
    def exitJoin_clause(self, ctx:sqlParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by sqlParser#join_operator.
    def enterJoin_operator(self, ctx:sqlParser.Join_operatorContext):
        pass

    # Exit a parse tree produced by sqlParser#join_operator.
    def exitJoin_operator(self, ctx:sqlParser.Join_operatorContext):
        pass


    # Enter a parse tree produced by sqlParser#join_constraint.
    def enterJoin_constraint(self, ctx:sqlParser.Join_constraintContext):
        pass

    # Exit a parse tree produced by sqlParser#join_constraint.
    def exitJoin_constraint(self, ctx:sqlParser.Join_constraintContext):
        pass


    # Enter a parse tree produced by sqlParser#select_core.
    def enterSelect_core(self, ctx:sqlParser.Select_coreContext):
        pass

    # Exit a parse tree produced by sqlParser#select_core.
    def exitSelect_core(self, ctx:sqlParser.Select_coreContext):
        pass


    # Enter a parse tree produced by sqlParser#compound_operator.
    def enterCompound_operator(self, ctx:sqlParser.Compound_operatorContext):
        pass

    # Exit a parse tree produced by sqlParser#compound_operator.
    def exitCompound_operator(self, ctx:sqlParser.Compound_operatorContext):
        pass


    # Enter a parse tree produced by sqlParser#signed_number.
    def enterSigned_number(self, ctx:sqlParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by sqlParser#signed_number.
    def exitSigned_number(self, ctx:sqlParser.Signed_numberContext):
        pass


    # Enter a parse tree produced by sqlParser#literal_value.
    def enterLiteral_value(self, ctx:sqlParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by sqlParser#literal_value.
    def exitLiteral_value(self, ctx:sqlParser.Literal_valueContext):
        pass


    # Enter a parse tree produced by sqlParser#unary_operator.
    def enterUnary_operator(self, ctx:sqlParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by sqlParser#unary_operator.
    def exitUnary_operator(self, ctx:sqlParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by sqlParser#column_alias.
    def enterColumn_alias(self, ctx:sqlParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by sqlParser#column_alias.
    def exitColumn_alias(self, ctx:sqlParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by sqlParser#keyword.
    def enterKeyword(self, ctx:sqlParser.KeywordContext):
        pass

    # Exit a parse tree produced by sqlParser#keyword.
    def exitKeyword(self, ctx:sqlParser.KeywordContext):
        pass


    # Enter a parse tree produced by sqlParser#name.
    def enterName(self, ctx:sqlParser.NameContext):
        pass

    # Exit a parse tree produced by sqlParser#name.
    def exitName(self, ctx:sqlParser.NameContext):
        pass


    # Enter a parse tree produced by sqlParser#database_name.
    def enterDatabase_name(self, ctx:sqlParser.Database_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#database_name.
    def exitDatabase_name(self, ctx:sqlParser.Database_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#schema_name.
    def enterSchema_name(self, ctx:sqlParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#schema_name.
    def exitSchema_name(self, ctx:sqlParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#table_function_name.
    def enterTable_function_name(self, ctx:sqlParser.Table_function_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#table_function_name.
    def exitTable_function_name(self, ctx:sqlParser.Table_function_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#table_name.
    def enterTable_name(self, ctx:sqlParser.Table_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#table_name.
    def exitTable_name(self, ctx:sqlParser.Table_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#column_name.
    def enterColumn_name(self, ctx:sqlParser.Column_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#column_name.
    def exitColumn_name(self, ctx:sqlParser.Column_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#collation_name.
    def enterCollation_name(self, ctx:sqlParser.Collation_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#collation_name.
    def exitCollation_name(self, ctx:sqlParser.Collation_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#index_name.
    def enterIndex_name(self, ctx:sqlParser.Index_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#index_name.
    def exitIndex_name(self, ctx:sqlParser.Index_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#table_alias.
    def enterTable_alias(self, ctx:sqlParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by sqlParser#table_alias.
    def exitTable_alias(self, ctx:sqlParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by sqlParser#any_name.
    def enterAny_name(self, ctx:sqlParser.Any_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#any_name.
    def exitAny_name(self, ctx:sqlParser.Any_nameContext):
        pass



del sqlParser