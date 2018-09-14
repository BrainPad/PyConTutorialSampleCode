# -*- coding: utf-8 -*-

def file_reader():
    # sushineta.txtを読み込み専用で開く
    f = open('sushineta.txt', mode='r', encoding='utf-8')
    # read関数でファイル全体を文字列として読み込む
    data = f.read()
    # ファイルを閉じる(リソースの解放)
    f.close()
    print(data)

def file_reader_2():
    f = open('sushineta.txt', mode='r', encoding='utf-8')
    # readline関数で一行だけ読み込む
    data = f.readline()
    f.close()
    print(data)

def file_reader_3():
    f = open('sushineta.txt', mode='r', encoding='utf-8')
    # readlines関数でファイル全体を配列として読み込む
    data = f.readlines()
    f.close()
    print(data)

file_reader()
file_reader_2()
file_reader_3()
