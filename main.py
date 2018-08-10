#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import click
from pcpp import Pcpp

@click.command()
@click.option('-d', '--def-macro', multiple=True)
@click.argument('file')
def main(def_macro, file):
    script = get_script(file)

    cpp = Pcpp(list(def_macro))

    res = cpp.run(script)

    sys.stdout.write(res)

def get_script(path):
    current_path = os.getcwd()
    file_path = os.path.join(current_path, path)

    with open(file_path) as f:
        return f.read()

if __name__ == '__main__':
    main()
