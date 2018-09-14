# -*- coding: utf-8 -*-

# デコレーターを使うと関数の中身を書き換えなくても機能を追加すること出来ます
# デコレーターは"@xxx"(xxxは機能名)で表します
def show_message(f): # 関数(今回の例ではspam1関数)を受け取る
    def wrapper():
        print("function called")
        return f() # 関数を実行する
    return wrapper # wrapper関数の実行結果を返す

# デコレーターが使われているため"function called"が呼び出される
# 擬似的に書くと spam1関数 = show_message(spam1)という呼び出され方をしている
@show_message
def spam1():
    print("spam1 called")

# デコレーターが使われていないため"function called"は呼び出されない
def spam2():
    print("spam2 called")

if __name__ == '__main__':
    spam1()
    print("------------")
    spam2()
