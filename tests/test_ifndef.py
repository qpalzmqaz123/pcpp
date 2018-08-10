#!/usr/bin/env python3
# coding: utf-8

from .base import BaseTest

class TestIfndef(BaseTest):

    def setup(self):
        self.def_macro = ['A', 'B']

    def teardown(self):
        pass

    def test_without_else(self, res):
        '''\
        1
        #ifndef A
        2
        #endif
        3\
        '''
        assert res == '\n'.join(['1', '3'])

    def test_else(self, res):
        '''\
        1
        #ifndef A
        2
        #else
        3
        #endif
        4\
        '''
        assert res == '\n'.join(['1', '3', '4'])

    def test_nested_ifndef_else(self, res):
        '''\
        1
        #ifndef A
        2
        #else
        3
        #ifndef B
        4
        #endif
        5
        #endif
        6\
        '''
        assert res == '\n'.join(['1', '3', '5', '6'])

    def test_nested_ifndef_else(self, res):
        '''\
        1
        #ifndef A
        2
        #else
        3
        #ifndef B
        4
        #else
        5
        #ifdef C
        6
        #endif
        7
        #endif
        8
        #endif
        9\
        '''
        assert res == '\n'.join(['1', '3', '5', '#ifdef C', '6', '#endif', '7', '8', '9'])
