# -*- coding: utf-8 -*-

# 例外が発生してもしなくても最後に実行される処理はfinally文を使う
x = '5'
try:
    print(x + 1) # 文字列と数値の加算のため例外(TypeError)が発生する
except TypeError: # TypreError発生時の処理を記述する
    print('型が違います')
except IndexError:
    print('リストに対して存在しないインデックスを指定しています')
except:
    print('何かがおかしいです')
else:
    print('else文が実行されました')
finally:
    print('finally文が実行されました')
