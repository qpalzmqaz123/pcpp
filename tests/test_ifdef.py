#!/usr/bin/env python3
# coding: utf-8

from .base import BaseTest

class TestIfdef(BaseTest):

    def setup(self):
        self.def_macro = ['A', 'B']

    def teardown(self):
        pass

    def test_without_else(self, res):
        '''\
        1
        #ifdef A
        2
        #endif
        3\
        '''
        assert res == '\n'.join(['1', '2', '3'])

    def test_else(self, res):
        '''\
        1
        #ifdef A
        2
        #else
        3
        #endif
        4\
        '''
        assert res == '\n'.join(['1', '2', '4'])

    def test_nested_ifdef_without_else(self, res):
        '''\
        1
        #ifdef A
        2
        #ifdef B
        3
        #endif
        4
        #endif
        5\
        '''
        assert res == '\n'.join(['1', '2', '3', '4', '5'])

    def test_nested_ifdef_without_else_1(self, res):
        '''\
        1
        #ifdef A
        2
        #ifdef C
        3
        #endif
        4
        #endif
        5\
        '''
        assert res == '\n'.join(['1', '2', '#ifdef C', '3', '#endif', '4', '5'])

    def test_nested_ifdef_without_else_2(self, res):
        '''\
        1
        #ifdef A
        2
        #ifdef C
        3
        #ifdef B
        4
        #endif
        5
        #endif
        6
        #endif
        7\
        '''
        print(res)
        assert res == '\n'.join(['1', '2', '#ifdef C', '3', '4', '5', '#endif', '6', '7'])
