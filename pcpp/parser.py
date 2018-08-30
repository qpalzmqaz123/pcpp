#!/usr/bin/env python3
# coding: utf-8

import sys
import ply.yacc as yacc
from . import lexer
from . import ast

tokens = lexer.tokens

def p_program(p):
    '''program : stmt_list'''
    p[0] = p[1]

def p_stmt_list(p):
    '''stmt_list : stmt
                 | stmt_list stmt'''
    if len(p) == 2:
        p[0] = ast.Block().append(p[1])
    else:
        p[0] = p[1].append(p[2])

def p_stmt_ifdef_endif(p):
    '''stmt : expr_stmt NEWLINE
            | macro_stmt NEWLINE
            | NEWLINE'''
    if len(p) > 2:
        p[0] = p[1]

def p_expr_stmt_identifer(p):
    '''expr_stmt : IDENTIFER
                 | expr_stmt IDENTIFER'''
    pass

def p_macro_stmt_ifdef_endif(p):
    '''macro_stmt : IFDEF IDENTIFER stmt_list ENDIF'''
    p[0] = ast.If(ast.If.DEF, p[2], p[3], None, p.lineno(1), None, p.lineno(4))

def p_macro_stmt_ifdef_else_endif(p):
    '''macro_stmt : IFDEF IDENTIFER stmt_list ELSE stmt_list ENDIF'''
    p[0] = ast.If(ast.If.DEF, p[2], p[3], p[5], p.lineno(1), p.lineno(4), p.lineno(6))

def p_macro_stmt_ifndef_endif(p):
    '''macro_stmt : IFNDEF IDENTIFER stmt_list ENDIF'''
    p[0] = ast.If(ast.If.NDEF, p[2], p[3], None, p.lineno(1), None, p.lineno(4))

def p_macro_stmt_ifndef_else_endif(p):
    '''macro_stmt : IFNDEF IDENTIFER stmt_list ELSE stmt_list ENDIF'''
    p[0] = ast.If(ast.If.NDEF, p[2], p[3], p[5], p.lineno(1), p.lineno(4), p.lineno(6))

def p_error(p):
    if p:
        raise Exception("Syntax error at '%s' line %d column %d" % (p.value, p.lineno, p.lexpos + 1))
    else:
        raise Exception("Syntax error")

def parse(script):
    _lexer = lexer.get_lexer()
    parser = yacc.yacc(debug=0, outputdir="/tmp", tabmodule="pcpp")

    return parser.parse(script, lexer=_lexer)
