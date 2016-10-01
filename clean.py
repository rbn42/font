#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
消除setofont中空白的字符,让其他字符填补进来.

Usage:
  main.py <font-file> <new-font-name>

Options:
  -h --help     Show this screen.
"""

import fontforge
import os
import shutil
import re


def clean(src):
    for char in src:
        if src[char].foreground.isEmpty():
            l = re.findall('uni([0-9A-F]+)', char)
            if len(l) < 1:
                continue
            i = int(l[0], 16)
            if i == 8237:
                # 影响字高的字符
                # Unicode Character 'LEFT-TO-RIGHT OVERRIDE' (U+202D)
                continue
            src.selection.select(("more", None), char)
    src.cut()

from docopt import docopt
arguments = docopt(__doc__)
file_ = arguments['<font-file>']
newfontname = arguments['<new-font-name>']

font = fontforge.open(file_)

clean(font)

print('save')
filename = '%s.sfd' % newfontname
font.save(filename)

print('generate ttf')
filename = '%s.ttf' % newfontname
font.generate(filename)
