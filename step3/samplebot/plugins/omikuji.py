# -*- coding: utf-8 -*-
import random

from slackbot.bot import respond_to

OMIKUJI_LIST = [
    '大吉',
    '中吉',
    '吉',
    '末吉',
    '凶',
    '大凶',
]


@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(OMIKUJI_LIST))
