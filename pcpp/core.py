#!/usr/bin/env python3
# coding: utf-8

from . import parser

class Pcpp(object):

    def __init__(self, def_macros):
        self._def_macros = def_macros

    def run(self, script):
        tree = parser.parse(script)

        lst = tree.get_del_lines(self._def_macros)

        print(lst)
