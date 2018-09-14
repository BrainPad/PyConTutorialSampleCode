# -*- coding: utf-8 -*-
import random


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


# 敵の属性 (攻撃力)
class Enemy:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack


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
def check_hero(job, age):
    if job == "勇者" and age >= 16:
        return True, "では魔王を退治してきてください"
    elif job == "勇者" or age >= 16:
        return False, "もう少し頑張ってください"
    else:
        return False, "頑張ってください"


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


def check_friend(my, job_name):
    result = False
    for friend in my.friend_lst:
        if job_name == friend.job:
            result = True
    return result


# 敵と対戦します
def battle(hero, enemy):
    # 体調を -10 〜 10 で表します
    pep = random.randint(-10, 10)

    # 主人公が戦います (攻撃力 = 年齢 + 体調)
    if hero.age + pep > enemy.attack:
        return True

    # 主人公が負けた場合は仲間が戦います
    for friend in hero.friend_lst:
        if friend.age + pep > enemy.attack:
            return True

    # 仲間が全滅したら負けです
    return False


if __name__ == "__main__":
    # ゲーム開始させます
    game_manager = GameManager()
    game_manager.start()

    # 勇者を誕生させます
    hero = Character('ロト', '勇者', 16)

    # 勇者の条件をチェックします
    print('こんにちは' + hero.name)
    print('職業は' + hero.job)
    print('年齢は' + str(hero.age))

    hero_check, mes = check_hero(hero.job, hero.age)
    if hero_check:
        print(mes)
    else:
        game_manager.end()

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
    friend_check = check_friend(my=hero, job_name='魔法使い')
    if not friend_check:
        game_manager.end()

    if game_manager.end_flg:
        print('お疲れ様でしたゲームは終了です')
        exit()

    # 敵を登場させます
    enemy = Enemy('悪魔', 15)
    print(enemy.name + 'が現れた')

    # 敵と対戦します
    won = battle(hero, enemy)
    if won:
        print(hero.name + 'は勝利した！')
    else:
        print(hero.name + 'は負けてしまった...')
        game_manager.end()

    if game_manager.end_flg:
        print('お疲れ様でしたゲームは終了です')
        exit()

    print('ゲームは続きます')
