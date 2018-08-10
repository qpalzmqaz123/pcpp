#!/usr/bin/env python3
# coding: utf-8

from .base import BaseTest

class TestMisc(BaseTest):

    def setup(self):
        self.def_macro = ['A', 'B']

    def teardown(self):
        pass

    def test_1(self, res):
        '''\
        1
        #ifndef A
        2
        #else
        3
        #endif
        4
        #ifdef B
        5
        #else
        6
        #endif
        7\
        '''
        assert res == '\n'.join(['1', '3', '4', '5', '7'])
