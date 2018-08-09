#!/usr/bin/env python
# coding: utf-8

import sys
import ply.lex as lex

tokens = [
    'IDENTIFER',
    'IFDEF', 'IFNDEF', 'ELSE', 'ENDIF',
    'NEWLINE'
]

t_IDENTIFER = r'[a-zA-Z_][a-zA-Z_0-9]*'

t_IFDEF  = r'\#ifdef'
t_IFNDEF = r'\#ifndef'
t_ELSE   = r'\#else'
t_ENDIF  = r'\#endif'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_COMMENT(t):
    r'(/\*[^\*/]*?\*/)|(//.*)'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    script = sys.stdin.read()

    lexer.input(script)

    while True:
        tok = lexer.token()
        if not tok:
            break

        print(tok)
