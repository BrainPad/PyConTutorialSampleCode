# -*- coding: utf-8 -*-

# ループ文で例外が発生せずに最後まで進んだ時の処理はelse文を使う
team = ['ichiro', 'jiro', 'saburo']

for i in team:
    print(i)
else:
    print('else文が実行されました')

# break文によって中断された場合はelse文は実行されない
for j in team:
    print(j)
    break
else:
    print('else文が実行されました')

# try-except文でも同様
x = 5

try:
    print(x + 1) # 文字列と数値の加算のため例外(TypeError)が発生する
    # a = []; a[1] # 配列の範囲外のため例外(IndexError)が発生する
    # 100 / 0 # 除算出来ないため例外(ZeroDivisionError)が発生する
except TypeError: # TypreError発生時の処理を記述する
    print('型が違います')
except IndexError: # IndexError発生時の処理を記述する
    print('リストに対して存在しないインデックスを指定しています')
except: # 上記以外の例外発生時の処理を記述する
    print('何かがおかしいです')
else:
    print('else文が実行されました')
