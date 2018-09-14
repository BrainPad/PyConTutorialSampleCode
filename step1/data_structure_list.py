# -*- coding: utf-8 -*-

# リストの初期化
lst_1 = ['a', 2, 1.0]
lst_2 = ['b', 2]

# リストの中身を表示する
print("変数 lst_1 :" + str(lst_1))
print("変数 lst_2 :" + str(lst_2))

# リストから要素の取り出し
print("0番目の要素の取り出し:" + lst_1[0])

# リストの連結
lst = lst_1 + lst_2
print("lst_1とlst_2の連結結果:" + str(lst))

# リストから要素を変更する
lst[2] = 'c'
print("lstの2番目の要素を文字列のｃに変更する:" + str(lst))

# リストに要素を追加する
lst.insert(5, 'z')
print('lstの最後に文字列のｚを追加する' + str(lst))

# リストの要素を削除する
lst.remove(2)
print('lstの最初の要素2を削除する' + str(lst))

# リストからインデックスを指定して削除する
del lst[1]
print('1番目の要素を削除する' + str(lst))
