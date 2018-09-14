# -*- coding: utf-8 -*-
""" 関数化前後の例を
数字の大小を比較を
題材にして記述する
"""
# 関数化前
print("関数にする前の処理 開始")
x = 3
y = 5

if x >= y:
    print(x)
else:
    print(y)
print("関数にする前の処理 終了\n")


# 関数の定義1（戻り値あり）
print("関数（戻り値あり）にした後の処理 開始")
def get_absolute_value(x, y):
    if x >= y:
        return x
    else:
        return y

# 呼び出し元
large_number = get_absolute_value(3, 5)
print(large_number)
print("関数（戻り値あり）にした後の処理 終了\n")


# 関数の定義（戻り値なし）
print("戻り値なしの関数 開始")
def custom_print(value1):
    print("引数は：" + value1)

custom_print('pycon2018')
print("戻り値なしの関数 終了\n")
