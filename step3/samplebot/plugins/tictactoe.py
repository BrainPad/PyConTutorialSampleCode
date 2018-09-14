# -*- coding: utf-8 -*-
import random

from slackbot.bot import respond_to

from .libs.tictactoe import Board, Player


class Game:
    def __init__(self, user, board):
        self.user = user
        self.board = board


game = Game(None, Board())


@respond_to('三目並べ')
def tictactoe_play(message):
    if game.user is not None:
        message.reply(f'{game.user} さんがプレイしています')
    else:
        game.user = message.user['name']
        game.board.setup(size=3, players=[Player(':o:'), Player(':x:')])

    message.reply(f'\nあなたは {game.board.players[0]}、'
                  f'私は {game.board.players[1]} です\n'
                  f'{game.board}\n座標をどうぞ')


@respond_to(r'(\d+)')
def tictactoe_put(message, n):
    if game.user != message.user['name']:
        return

    is_next_tern = _tictactoe_put(message, int(n))

    if is_next_tern:
        _tictactoe_put(message)


def _tictactoe_put(message, n=None):
    """プレイヤーが三目並べボードにマークを置く

    座標 n にマークを置く。
    座標 n を指定しない場合、ボード上の置ける場所にランダムにマークが置かれる。
    マークを置いたあとにゲームが終了した場合は、どちらかの勝ち、または引き分けを返事をする。
    ゲームが続行している場合は次のプレイヤーターンに変える。

    Args:
        message: SlackBot message オブジェクト
        n: ボードの座標, None の場合はランダムに選択される

    Returns:
        True 次のターンに進んだ場合。それ以外は False
    """
    if n is None:
        game.board.put(*random.choice(game.board.puttables))
    else:
        if game.board.put_n(n) is None:
            message.reply(f'{n} には置けません')
            return False

    if game.board.won():
        message.reply(f'\n{game.board}\n{game.board.player} の勝ちです')
        game.user = None
        return False

    if game.board.is_end():
        message.reply(f'\n{game.board}\n引き分けです')
        game.user = None
        return False

    game.board.switch_player_turn()
    message.reply(f'\n{game.board}')
    return True
