# -*- coding: utf-8 -*-
from slackbot.bot import respond_to


@respond_to('こんにちは')
def hello(message):
    message.reply('こんにちは')
