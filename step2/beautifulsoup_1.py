# -*- coding: utf-8 -*-

# pip install beautifulsoup4 が必要です
from bs4 import BeautifulSoup


SAMPLE_HTML = """
<html>
<head>
  <title>タイトル！</title>
</head>
<body>
  <h1>見出し</h1>
  <p>本文1</p>
  <p>本文2</p>
</body>
</html>
"""


if __name__ == "__main__":
    soup = BeautifulSoup(SAMPLE_HTML, 'html.parser')

    # HTMLタグ要素を指定して取得
    print(soup.title)
    # .stringで中身のテキストだけを取得
    print(soup.h1.string)
    # p要素は複数あるけどどうなる？
    print(soup.p.string)

    print('--')

    # すべてのp要素を取得
    for p in soup.find_all('p'):
        print(p.string)
