# -*- coding: utf-8 -*-

import sqlite3


if __name__ == "__main__":
    # sqlite database に接続
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # テーブルの作成
    c.execute("CREATE TABLE IF NOT EXISTS sample_table (id INTEGER, name TEXT, age int)")
    # データの挿入
    c.execute("INSERT INTO sample_table VALUES (1, 'ブレイン太郎', 20)")
    c.execute("INSERT INTO sample_table VALUES (2, 'ブレイン花子', 17)")
    # SQLデータの確定
    conn.commit()

    # 挿入したデータの確認
    results = c.execute("SELECT * FROM sample_table")
    for row in results:
        print(row)

    print("--")

    # データを整形して表示
    results = c.execute("SELECT * FROM sample_table")
    for row in results:
        print("出席番号{}番の{}さんは{}歳です。".format(row[0], row[1], row[2]))

    # sqlite database 接続の終了
    conn.close()
