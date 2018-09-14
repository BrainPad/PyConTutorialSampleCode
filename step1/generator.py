# -*- coding: utf-8 -*-

# ジェネレータ式
print('ジェネレータ式　開始')
num = (str(x) + '番' for x in range(10) if x > 2)
for n in num:
    print(n)
print('ジェネレータ式　終了\n')

# リスト内包表記
print('リスト内包表記　開始')
num = [str(x) + '話' for x in range(10) if x > 5]
for n in num:
    print(n)
print('リスト内包表記　終了\n')


# ジェネレータ
print('ジェネレータ　開始')
def do_yield():
    yield 'one'
    yield 'two'
    yield 'three'

for v in do_yield():
    print(v)
print('ジェネレータ　終了')