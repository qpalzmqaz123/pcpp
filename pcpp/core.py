#!/usr/bin/env python3
# coding: utf-8

from . import parser

class Pcpp(object):

    def __init__(self, def_macros):
        self._def_macros = def_macros

    def run(self, script):
        tree = parser.parse(script)

        lst = tree.get_del_lines(self._def_macros)

        lines = script.split('\n')

        def _(x):
            x += 1

            for rg in lst:
                if x >= rg.start and x <= rg.end:
                    return False

            return True

        lines = [v for i, v in enumerate(lines) if _(i)]

        return '\n'.join(lines)
