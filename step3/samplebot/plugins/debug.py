# -*- coding: utf-8 -*-
import json

from slackbot.bot import respond_to


@respond_to('debug')
def hoge(message):
    text = '\n'
    for k, v in inspect_message(message).items():
        text += '*message.{}*\n'.format(k)
        text += quote_code(format_dict(v)) + '\n'
    message.reply(text)


def inspect_message(message):
    dicts = {}
    for key in dir(message):
        if not key.startswith('_'):
            attr = getattr(message, key)
            if isinstance(attr, dict):
                dicts[key] = attr
    return dicts


def format_dict(d):
    return json.dumps(d, indent=2, ensure_ascii=False)


def quote_code(text):
    return '```{}```'.format(text)
