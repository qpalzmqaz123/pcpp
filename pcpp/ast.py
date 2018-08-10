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

    def __lt__(self, b):
        if self.start < b.start:
            return True
        else:
            return self.end < b.end

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

        return m[0] if m else m

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
        if self.elseline != None:
            lst.append(Range(self.elseline, self.elseline))
        lst.append(Range(self.endline, self.endline))

        if reserve_leaf:
            lst.extend(reserve_leaf.get_del_lines(def_macros))

        if delete_leaf:
            if self.type == self.DEF:
                lst.append(Range(self.elseline, self.endline))
            else:
                if self.elseline == None:
                    lst.append(Range(self.ifline, self.endline))
                else:
                    lst.append(Range(self.elseline, self.endline))

        return self._uniq(lst)

    def _uniq(self, lst):
        if not lst:
            return lst

        max_end = max([x.end for x in lst])

        def is_del(x):
            for rg in lst:
                if x >= rg.start and x <= rg.end:
                    return True

            return False

        del_map = map(is_del, range(0, max_end + 1))

        rgs = []
        state = 'wait' # wait | start
        for index, is_del in enumerate(del_map):
            if state == 'wait':
                if is_del:
                    rgs.append(Range(index, None))
                    state = 'start'
            elif state == 'start':
                if is_del == False:
                    rgs[-1].end = index - 1
                    state = 'wait'
            else:
                raise Exception('Unknow state: %s' % state)

        if rgs[-1].end == None:
            rgs[-1].end = max_end

        return rgs
