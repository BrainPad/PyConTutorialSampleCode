# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup


url = 'https://news.yahoo.co.jp/'


if __name__ == "__main__":
    response = urllib.request.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    # アクセスランキングTOP5を抽出して表示
    for element in soup.find_all('dt', class_='ttl')[0:5]:
        print(element.text.strip())
