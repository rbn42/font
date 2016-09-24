#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Hello.

Usage:
  main.py <font-file-1> <font-file-2> <new-font-name>

Options:
  -h --help     Show this screen.
"""
# 金 37329 91D1
# 为 20026 4E3A
# 额 39069 989D

"""
字体文件,有太多细节要处理,简单的合并两个字体后,没法用
"""
import fontforge


def copy(src, dst):
    for char in src:
        if not src[char].foreground.isEmpty():
            if char not in dst:
                # TODO 暂且做不到统一dst和src的字体范围.
                print(char)
                continue
            src.selection.select(("more", None), char)
            dst.selection.select(("more", None), char)
    src.copy()
    dst.paste()

from docopt import docopt
arguments = docopt(__doc__)
file1 = arguments['<font-file-1>']
file2 = arguments['<font-file-2>']
newfontname = arguments['<new-font-name>']

font1 = fontforge.open(file1)
font2 = fontforge.open(file2)

font2.fontname = newfontname

copy(font1, font2)

print('save')
filename = '%s.sfd' % newfontname
font2.save(filename)

print('generate ttf')
filename = '%s.ttf' % newfontname
font2.generate(filename)

print('generate ttc')
filename = '%s.ttc' % newfontname
font2.generateTtc(filename, None)

print('generate otf')
filename = '%s.otf' % newfontname
font2.generate(filename)
