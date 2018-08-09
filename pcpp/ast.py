#!/usr/bin/env python3
# coding: utf-8

class Tree(object):

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__, str(self.__dict__))

    def __str__(self):
        return self.__repr__()

class Block(Tree):

    def __init__(self):
        self.list = []

    def append(self, node):
        if node:
            self.list.append(node)

        return self

    def __repr__(self):
        if not self.list:
            return '%s()' % type(self).__name__
        else:
            arr = ['']
            arr.append(type(self).__name__ + '(')

            for node in self.list:
                arr.append('  %s' % str(node))

            arr.append(')')

            return '\n'.join(arr)

class Node(Tree):
    pass

class If(Node):
    DEF = 'def'
    NDEF = 'ndef'

    def __init__(self, type, var, body, otherwise, ifline, elseline, endline):
        self.type = type
        self.var = var
        self.body = body
        self.otherwise = otherwise
        self.ifline = ifline
        self.elseline = elseline
        self.endline = endline

    ## XXX: calc delete lines
