
# クラスの定義(空クラス)
class MyClass1:
    pass

print('クラスのメソッドについて 開始')

# クラスの関数
class MyClass2:

    def myclass_method(self):
        print('MyClassのメソッド')

instance_2 = MyClass2()
instance_2.myclass_method()

print('クラスのメソッドについて 終了\n')


print('属性の参照と変更 開始')

# 属性の参照と変更
class MyClass3:

    def display(self):
        print('名前は:' + self.name)

instance_3 = MyClass3()
instance_3.name = 'python'
instance_3.display()
instance_3.name = 'java'
instance_3.display()

print('属性の参照と変更 終了\n')

print('__init__メソッド 開始')

# __init__関数での初期化
class MyClass4:

    def __init__(self, name):
        self.name = name

    def display(self):
        print('名前は:' + self.name)

instance_4 = MyClass4('python')
instance_4.display()

print('__init__メソッド 終了')
