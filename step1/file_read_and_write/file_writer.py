# -*- coding: utf-8 -*-

def file_writer():
    # sushineta.txtを読み込み専用で開く
    f = open('sushineta_2.txt', mode='w', encoding='utf-8')
    # 文字列'トロ'をファイルに書き込む
    f.write('トロ')
    f.write('\n')
    # ファイルを閉じる(リソースの解放)
    f.close()

def file_writer_2():
    # sushineta.txtを読み込み専用で開く
    f = open('sushineta_2.txt', mode='a', encoding='utf-8')
    # 文字列'サーモン'をファイルに追記する
    f.write('サーモン')
    f.close()

file_writer()
file_writer_2()
