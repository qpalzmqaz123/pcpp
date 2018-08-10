# PCPP

Python c preprocessor

## Installation

```bash
python3 setup.py install
```

## Usage

```bash
Usage: pcpp [OPTIONS] FILE

Options:
  -d, --def-macro TEXT
  --help                Show this message and exit.
```

## Example

test.c
```c
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
7
```

```bash
pcpp -d A -d B test.c
```

will print:

```bash
1
3
4
5
7
```
