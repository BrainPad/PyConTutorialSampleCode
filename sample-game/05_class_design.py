# -*- coding: utf-8 -*-


# 登場人物の属性（職業、年齢、etc）
class Character:

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
        self.equipment = None
        self.friend_lst = []

    def append_friend(self, other):
        self.friend_lst.append(other)


# 道具の属性（剣、盾、お金）
class Bag:
    def __init__(self):
        self.weapon = None
        self.shield = None
        self.gold = 0


# ゲームの状態を管理します
class GameManager:
    def __init__(self):
        self.end_flg = True

    def start(self):
        self.end_flg = False

    def end(self):
        self.end_flg = True


# 勇者としての条件をチェックします
def check_hero(chara, mgr):
    print('こんにちは' + chara.name)
    print('職業は' + chara.job)
    print('年齢は' + str(chara.age))
    if chara.job == "勇者" and hero.age >= 16:
        print("では魔王を退治してきてください")
    elif hero.job == "勇者" or hero.age >= 16:
        print("もう少し頑張ってください")
        mgr.end()
    else:
        print("頑張ってください")
        mgr.end()


# 道具をプレゼントします
def present_equipment(chara):
    bag = Bag()
    bag.gold = 100
    print("勇者は" + str(bag.gold) + "Goldを手に入れた")
    bag.shield = '盾'
    print("勇者は" + bag.shield + "を手に入れた")
    bag.weapon = '剣'
    print("勇者は" + bag.weapon + "を手に入れた")
    chara.equipment = bag


def check_friend(my, job_name, mgr):
    result = False
    for friend in my.friend_lst:
        if job_name == friend.job:
            result = True
    if not result:
        mgr.end()


if __name__ == "__main__":
    # ゲーム開始させます
    game_manager = GameManager()
    game_manager.start()

    # 勇者を誕生させます
    hero = Character('ロト', '勇者', 16)

    # 勇者の条件をチェックします
    check_hero(chara=hero, mgr=game_manager)
    if game_manager.end_flg:
        print('お疲れ様でしたゲームは終了です')
        exit()

    # 勇者に装備を渡します
    present_equipment(chara=hero)

    # 勇者に魔法使いが仲間になります
    wizard = Character('花子', '魔法使い', 16)
    hero.append_friend(wizard)
    print(hero.name + 'に' + wizard.name + 'が仲間になった')

    # 勇者のメンバーに魔法つかいがいるかチェックします
    check_friend(my=hero, job_name='魔法使い', mgr=game_manager)
    if game_manager.end_flg:
        print('お疲れ様でしたゲームは終了です')
        exit()

    print('ゲームは続きます')
