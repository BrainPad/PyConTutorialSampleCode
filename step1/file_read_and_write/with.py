# -*- coding: utf-8 -*-

f = open('sushineta.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
print(data)

# with構文を用いると自動でリソースが解放される
with open('sushineta.txt', 'r', encoding='utf-8') as f:
    data = f.read()
print(data)
