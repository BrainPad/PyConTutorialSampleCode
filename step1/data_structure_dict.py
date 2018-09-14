# -*- coding: utf-8 -*-

# 辞書の初期化
my_dict_1 = {'key1': 1, 'key2': '鈴木'}

# 辞書の中身を表示する
print('辞書の中身は：' + str(my_dict_1))

# 辞書から要素の取り出し
print('key1の値は：' + str(my_dict_1['key1']))

# 辞書から要素を変更する
my_dict_1['key1'] = 2
print('key1を１から２に変更する：' + str(my_dict_1))

# 辞書に要素を追加する
my_dict_1['new_key'] = '新人'
print('辞書に新しい要素「new_key」を追加する：' + str(my_dict_1))

# 辞書の要素を削除する
del my_dict_1['key2']
print('辞書からkey2を削除する：' + str(my_dict_1))
