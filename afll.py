import ply.lex as lex
import ply.yacc as yacc


tokens =['ID','slash']
t_ignore=' '
t_ID=r'[.A-Za-z0-9_]+'
t_slash='\/'

def p_slash(p):
    '''assign : slash slash ID'''
    print("Correct Syntax!")

def p_error(p):
    print("Wrong Syntax!")

def t_error(p):
    print("Wrong Syntax1!")





lex.lex();
yacc.yacc();
data ='''/ Hello'''

yacc.parse(data)

# import ply.lex as lex
# import ply.yacc as yacc

# tokens =['next','do','while','openCurly','closeCurly','condition','statements','openBrac','closeBrac','semicolon']
# t_ignore='\t';
# t_next='\\n';
# t_do=r'do';
# t_while=r'while';
# t_openCurly=r'\{';
# t_closeCurly=r'\}';
# t_condition=r'condition';
# t_statements=r'statements';
# t_openBrac=r'\(';
# t_closeBrac=r'\)';
# t_semicolon=r';';

# def p_do(p):
#     '''assign : do expr'''
#     print("Correct Syntax!");

# def p_expr(p):
#     '''expr : statementsub next
#             | statementsub'''

# def p_statementsub(p):
#     '''statementsub : openCurly next statements semicolon next closeCurly whilesub'''

# def p_while(p):
#     '''whilesub : while conditionsub semicolon'''

# def p_conditionsub(p):
#     '''conditionsub : openBrac condition closeBrac'''

# def p_error(p):
#     print("Wrong Syntax!");

# def t_error(p):
#     print("Wrong Syntax1");

# lex.lex();
# yacc.yacc();


# data ='''do{
#     statements;
# }while(condition);''';

# yacc.parse(data)


# # import ply.lex as lex
# # import ply.yacc as yacc

# # tokens =['next','if','else','openCurl','closeCurl','condition','statements','openBrack','closeBrack','semicolon']
# # t_ignore=' \t';
# # t_next='\\n';
# # t_if=r'if';
# # t_else=r'else';
# # t_openCurl=r'\{';
# # t_closeCurl=r'\}';
# # t_condition=r'condition';
# # t_statements=r'statements';
# # t_openBrack=r'\(';
# # t_closeBrack=r'\)';
# # t_semicolon=r';';

# # def p_if(p):
# #     '''assign : if expr elsesub'''
# #     print("Correct Syntax!");

# # def p_expr(p):
# #     '''expr : conditionsub 
# #             '''

# # def p_else(p):
# #     '''elsesub : else statementsub '''

# # def p_conditionsub(p):
# #     '''conditionsub : openBrack condition closeBrack statementsub'''

# # def p_statementsub(p):
# #     '''statementsub : openCurl next statements semicolon next closeCurl
# #                     '''

# # def p_error(p):
# #     print("Wrong Syntax!");

# # def t_error(p):
# #     print("Wrong Syntax!");

# # lex.lex();
# # yacc.yacc();

# # data = '''if(condition){  
# #     statements;
# # } else{ 
# #     statements;
# # } ''';

# # yacc.parse(data)
