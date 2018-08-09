#!/usr/bin/env python3
# coding: utf-8

class Range(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return '(%s -> %s)' % (self.start, self.end)

    def __str__(self):
        return self.__repr__()

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

    def get_del_lines(self, def_macros=[]):
        m = [x.get_del_lines(def_macros) for x in self.list]
        m = [x for x in m if x]

        for x in m[1:]:
            m[0].extends(x)

        return m[0]

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
    def get_del_lines(self, def_macros=[]):
        '''
        return [(start, end), ...]
        '''
        if self.var not in def_macros:
            return []

        reserve_leaf = self.body if self.type == self.DEF else self.otherwise
        delete_leaf = self.body if reserve_leaf == self.otherwise else self.otherwise

        lst = []

        lst.append(Range(self.ifline, self.ifline))

        return lst
