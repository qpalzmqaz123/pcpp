#!/usr/bin/env python3
# coding: utf-8

from . import parser

class Pcpp(object):

    def __init__(self, def_macros):
        self._def_macros = def_macros

    def run(self, script):
        parser.parse(script)
