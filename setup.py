#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup

setup(
    name='pcpp',
    version='0.0.1',
    description='python c preprocessor',
    author='wangqj',
    author_email='qpalzmqaz123@gmail.com',
    url='',
    packages=['pcpp'],
    scripts=['bin/pcpp'],
    install_requires=[
        'ply',
        'click'
    ])
