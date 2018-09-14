# -*- coding: utf-8 -*-
import random

from slackbot.bot import respond_to

JANKEN_CHOICES = {
    'グー': ':fist:',  # グーの絵文字
    'チョキ': ':v:',  # チョキの絵文字
    'パー': ':hand:',  # パーの絵文字
}


@respond_to('(グー|チョキ|パー)')
def janken(message, shape):
    message.reply(choice())


def choice():
    """じゃんけんの絵文字からランダムに1つを返す"""
    emoji_list = list(JANKEN_CHOICES.values())
    return random.choice(emoji_list)
