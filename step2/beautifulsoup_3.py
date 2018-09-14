# -*- coding: utf-8 -*-

import os
import sqlite3
import urllib.request
from bs4 import BeautifulSoup


def get_feeds(url):
    # RSSフィードの取得
    response = urllib.request.urlopen(url)
    xml = response.read()

    soup = BeautifulSoup(xml, 'html.parser')

    # 結果格納用の箱を準備
    result = []
    # RSSを分解して今回必要な要素を結果に詰め込む
    for item in soup.find_all('item'):
        result.append({
            'title': item.title.text,
            'link': item['rdf:about'],
            'description': item.description.text,
        })

    return result


def save_db_feeds(feeds):
    # sqlite database に接続
    conn = sqlite3.connect('feeds.db')
    c = conn.cursor()

    # テーブルの作成
    c.execute("CREATE TABLE IF NOT EXISTS feeds_table (title text, link text, description text)")
    # データの挿入
    for item in feeds:
        c.execute("INSERT INTO feeds_table VALUES ('{}', '{}', '{}')".format(item['title'], item['link'], item['description']))
    # SQLデータの確定
    conn.commit()

    # sqlite database 接続の終了
    conn.close()


def get_db_feeds():
    # sqlite database に接続
    conn = sqlite3.connect('feeds.db')
    c = conn.cursor()

    res = c.execute("SELECT title, link, description FROM feeds_table")

    result = []
    for row in res:
        result.append({
            'title': row[0],
            'link': row[1],
            'description': row[2],
        })

    # sqlite database 接続の終了
    conn.close()

    return result


if __name__ == "__main__":
    # 出力用ファイルの準備
    this_script_path = os.path.dirname(os.path.abspath(__file__))
    output_html = os.path.join(this_script_path, 'output.html')


    # はてなブックマークの人気エントリ
    url = 'http://feeds.feedburner.com/hatena/b/hotentry'
    ### 他のRSSのだとうまくいくしょうか？
    # はてなブックマーク ITカテゴリ人気エントリ
    # url = 'http://b.hatena.ne.jp/hotentry/it.rss'
    # techcrunch
    # url = 'http://jp.techcrunch.com/feed/'


    feeds = get_feeds(url)

    ### 今回取得した結果を保存しておく？
    # save_db_feeds(feeds)

    ### 以前保存された結果も表示する？
    # saved_feeds = get_db_feeds()
    # feeds.extend(saved_feeds)

    # 結果を保存
    with open(output_html, 'w') as f:
        for item in feeds:
            f.write('<h2><a href="{}">{}</a></h2><p>{}</p>'.format(item['link'], item['title'], item['description']))

    print('ブラウザで下記のpathにアクセス！')
    print('file://' + output_html)
