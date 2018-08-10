#!/usr/bin/env python3
# coding: utf-8

from pcpp import Pcpp

def case(fn):
    def wrapper(self):
        script = fn.__doc__
        if not script:
            raise TypeError('script is not defined')

        cpp = Pcpp(self.def_macro)
        res = cpp.run(script)

        res = '\n'.join([x.strip() for x in res.split('\n')])

        fn(self, res)

    return wrapper

class MetaTest(type):

    def __new__(cls, clsname, bases, dct):
        if clsname != 'BaseTest':
            for (key, value) in dct.items():
                if key.startswith('test'):
                    dct[key] = case(value)

        return type.__new__(cls, clsname, bases, dct)

class BaseTest(object, metaclass=MetaTest):
    pass
