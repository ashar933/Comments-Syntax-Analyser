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
