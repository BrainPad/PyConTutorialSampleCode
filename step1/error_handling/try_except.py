# -*- coding: utf-8 -*-

x = '5'
y = [1]

try:
    print(x + 1) # 文字列と数値の加算のため例外(TypeError)が発生する
    print(y[1])
    raise Exception
except TypeError: # TypreError発生時の処理を記述する
    print('型が違います')
except IndexError: # IndexError発生時の処理を記述する
    print('リストに対して存在しないインデックスを指定しています')
except: # 上記以外の例外発生時の処理を記述する
    print('何かがおかしいです')
