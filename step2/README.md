# pep8

PEP8 とは Python のコードを読みやすくし、スタイルも統一するための規約です。
PEP とは Python Enhancement Proposal(Python 拡張提案)のことであり、
新機能の提案やガイドラインの説明などをするためのドキュメントです。

[PEP8 へのリンク](https://www.python.org/dev/peps/pep-0008/)

# ドキュメンテーション

関数定義の先頭では関数の内容を説明する文字列を書くことが出来ます。これを docstring (ドックストリング) と言います。

```
def my_func(left, right):
    """2 つの関数の和を返す
    ただし値がマイナスの場合は-1 をかけた値を返す
    """
    sum = left + right
    if sum < 0:
        return sum * -1
    else:
        return sum
```

また help 関数を使うことで docstring の内容を確認することが出来ます。

```
>>> help(my_func)


Help on function my_func in module test:

my_func(left, right)
    2 つの関数の和を返す
    ただし値がマイナスの場合は-1 をかけた値を返す
(END)
```

クラスも同様に書けます
```
class MyClass:
    """This is MyClass.
    This documente is example.
    """
    pass
```

# debug

実行時に `-m pdb` オプションを付与することで
ソースコードに変更を加えることなくデバッグを行うことが出来ます。

```
$ python -m pdb step2/debug/pdb_debug.py
> .../pycon/step2/debug/pdb_debug.py(3)<module>()
-> def fizzbuzz(num):
(Pdb) n  ← デバッガコマンド (次の行に移動する)
> .../pycon/step2/debug/pdb_debug.py(13)<module>()
-> for num in range(1, 21):
(Pdb) n
> .../pycon/step2/debug/pdb_debug.py(14)<module>()
-> print(fizzbuzz(num))
(Pdb) num
1
```

ソースコードの動作を 1 行づつ確認することが出来ます。
デバッガコマンド `n` を入力することで次の行に移動できます。

デバッガコマンドには他にも種類があります。詳細は[こちら](https://docs.python.jp/3/library/pdb.html#debugger-commands)を確認して下さい。

# setup.py

Python では自作したモジュールに setup.py を書くことで
他のファイルからインポートできるようになります。

setup.py の記述例はこちらです。

```
setup(
    name='sample',
    version='0.0.1',
    description='Sample package',
    long_description=readme,
    author='Sample Name',
    author_email='sample@sample.example',
    url='https://github.com/sample/package',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
```

# スクレイピング

Web サイトから情報を抽出するソフトウェアのこと。
クローラーとも呼ばれる。

## beautifulsoup とは？

HTML や XML ファイルからデータを取得するための Python ライブラリで、
ビューティフルスープ と読みます。

## スクリプトの動かし方

```sh
python beautifulsoup_1.py
```

エラーが出ると思います。
beautifulsoup は python に標準搭載されていない外部のライブラリなので、
別途インストールが必要になります。

```sh
pip install beautifulsoup4
```

再度動かすと、正常に動作するはずです。
日本語の処理結果的なものが表示されます。

```sh
python beautifulsoup_1.py
```

続けて 2 番目のスクリプトを動かしましょう。
日本語の文章が 5 行表示されます。

```sh
python beautifulsoup_2.py
```

* この日本語は何を意味しているでしょうか？
    * スクリプト内に URL があります。ブラウザで開いてみましょう
    * ブラウザで HTML ソースコードを見てみましょう
    * どの部分に取得した日本語があるでしょうか？
    * 取得する部分を変えてみるとどうなるでしょうか？

3 番目のスクリプトを動かし、表示された html のパスにアクセスしてみましょう。

```sh
python beautifulsoup_3.py
```

今回は RSS と呼ばれるフォーマットの Web ページを処理しています。
（RSS: ニュースやブログなど各種のウェブサイトの更新情報を配信するための文書フォーマットの総称）

* ブラウザで該当の URL を見てみましょう
* 表示されている部分はどこにあたるでしょうか？
* 表示していないが、他にも持っている情報としてどのようなものがあるでしょうか？
    * その情報も表示してみましょう！

* RSS の取得先を変えてみるとどうなるでしょうか？
    * うまくいかない場合、うまくいくようにコードを変更してみましょう

* 取得先を変えてみると、以前の結果は上書きして消えてしまいましたね
    * 取得した結果をデータベースに保存して、過去のものも表示できるようにしましょう
