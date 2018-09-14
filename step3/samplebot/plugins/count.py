# -*- coding: utf-8 -*-
from slackbot.bot import listen_to, respond_to


class PeopleCounter:
    """人数をカウントする

    Attributes:
        caller: 人数カウントを開始した人の名前
        title: カウントする内容 (例: 「ランチに行く人！」)
        members: 参加した人の一覧
    """

    def __init__(self):
        self.caller = None
        self.title = None
        self.members = set()  # 重複がないように set() を使う。 同じ人が何度参加しても1人としてカウント

    def setup(self, caller, title):
        """カウント情報を設定する

        Args:
            caller: 人数カウントを開始した人の名前
            title: カウントする内容
        """
        self.caller = caller
        self.title = title

    def add(self, name):
        """参加するメンバーを追加する

        Args:
            name: 参加する人の名前
        """
        self.members.add(name)

    def count(self):
        """参加人数を取得する

        Returns:
            参加人数
        """
        return len(self.members)

    def list(self):
        """参加する人の一覧

        Returns:
            参加する人の名前一覧をカンマで区切った文字列
        """
        return ', '.join(self.members)

    def clear(self):
        """カウント情報を削除する"""
        self.caller = None
        self.title = None
        self.members.clear()


# すべての関数から同じ値が見れるようにしたいので、global 領域で宣言する
people = PeopleCounter()


@respond_to('カウント(.*)')  # .* にはどんな文字列でもマッチ
def start_count(message, text):  # (.*) 内の文字が text 引数に入る
    if people.caller is None:
        people.setup(message.user['name'], text.strip())
        message.reply(f'「{people.title}」のカウントを開始します')
    else:
        message.reply(f'{people.caller}さんがカウント中です')


@listen_to('はい')
def add_member(message):
    if people.caller is not None:
        people.add(message.user['name'])
        message.react('ok')


@respond_to('締切')
def end_count(message):
    if people.caller is None:
        message.reply('カウントが開始されていません')
        return

    if people.caller == message.user['name']:
        text = (f'「{people.title}」のカウントを締め切りました\n'
                f'*人数* {people.count()}名\n'
                f'*参加者* {people.list()}\n')
        message.reply(text)
        people.clear()
    else:
        message.reply(f'{people.caller}さんがカウント中です')
