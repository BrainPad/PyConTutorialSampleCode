# -*- coding: utf-8 -*-

# 勇者のキャラクターメイキングをします
name = "ロト"
job = "勇者"

# 年齢を追加
age = 16

# 持ち物
bag = {}

# 仲間
friend = ['魔法使い']

# 終了フラグ
end_flg = False


# 職業が勇者で年齢が16歳以上でないと魔王退治出来ません。
print("あなたの名前は" + name + "で職業は" + job + "ですね")
print("年齢は" + str(age) + "ですね")

# 勇者のクエストを表示します
if job == "勇者" and age >= 16:
    print("では魔王を退治してきてください")
elif job == "勇者" or age >= 16:
    print("もう少し頑張ってください。お疲れ様でした")
    end_flg = True
else:
    print("お疲れ様でした")
    end_flg = True

if end_flg:
    print("冒険は終わりました")
    exit()

# 勇者に装備を与えます。
print("魔王を倒す装備を与えます")
bag['武器'] = '剣'
print("勇者は" + str(bag['武器']) + "を手に入れた")
bag['防具'] = '盾'
print("勇者は" + str(bag['防具']) + "を手に入れた")
bag['お金'] = 100
print("勇者は" + str(bag['お金']) + "GOLDを手に入れた")

# 勇者の仲間をチェックします。
if '魔法使い' not in friend:
    print("魔法使いがいません！！！")
    end_flg = True

if end_flg:
    print("冒険は終わりました")
    exit()
else:
    print("冒険は続きます")

