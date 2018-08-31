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
        #if aaa
        3
        #endif
        4
        #endif
        5\
        '''
        assert res == '\n'.join(['1', '2', '#if aaa', '3', '#endif', '4', '5'])

    def test_else(self, res):
        '''\
        1
        #ifdef A
        2
        #if aaa
        3
        #else
        4
        #endif
        5
        #endif
        6\
        '''
        assert res == '\n'.join(['1', '2', '#if aaa', '3', '#else', '4', '#endif', '5', '6'])
