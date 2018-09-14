# -*- coding: utf-8 -*-

a = 10
b = 20
c = 30
d = 40

if a > 5:
    print('aは5より大きい')
else:
    print('sorry')

if b < 10:
    print('bは10より小さい')
elif b >= 10 and b < 20:
    print('bは10以上20未満')
elif b >= 20:
    print('bは20以上')
else:
    print('sorry')

if c >= 30 or d < 30:
    print('論理和(cが合致)')

if d < 50:
    pass
