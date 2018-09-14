# -*- coding: utf-8 -*-

x = '5'
if not isinstance(x, int):
    raise TypeError('意図的に例外を発生させています')
    print('xは文字列型です')
