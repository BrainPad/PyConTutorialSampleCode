# -*- coding: utf-8 -*-


# while文
print('xが5より大きい場合終了します')
x = 1
while x <= 5:
    print('while文の内部処理:' + str(x))
    x += 1 # xに1を追加する
print('xが' + str(x) + 'となり外部処理になります\n')

# for文
# 配列での例
team_array = ['ichiro', 'jiro', 'saburo']
print('for文で繰り返す配列 開始：' + str(team_array))
for player in team_array:
    print(player)
print('for文で繰り返す配列 終了\n')

# 辞書型の例
team_dict = {1: 'ichiro', 2: 'jiro', 3: 'saburo'}
print('for文で繰り返す辞書  開始')
for k in team_dict:
    print(k, team_dict[k]) # keyとvalueを出力する
print('for文で繰り返す辞書 終了\n')

# range型を返す
# range型とは整数を要素とした変更不可な順序のある要素の集まりのこと
print('for文で繰り返すrange型  開始')
for i in range(5):
    print(i)
print('for文で繰り返すrange型 終了\n')

# ループを中断したい場合はbreak文を使う
print('for文で繰り返すrange型 break説明 開始')
for i in range(5):
    # 変数iが2より大きくなったらループを抜ける
    if i > 2:
        break
    print(i)
print('for文で繰り返すrange型  break説明 終了\n')

# 次のループへ強制的に進ませたい場合はcontinue文を使う
print('for文で繰り返すrange型 continue説明 開始')
for i in range(5):
    # 偶数は次のループへ進む(print文は実行されない)
    if i % 2 == 0:
        continue
    print(i)
print('for文で繰り返すrange型 continue説明 終了\n')

