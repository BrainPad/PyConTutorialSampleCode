# -*- coding: utf-8 -*-

NUMBER_ALPHA = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'keycap_ten',
]


class Player:
    """三目並べのプレイヤー

    Attributes:
        mark: このプレイヤーが置くマーク
    """

    def __init__(self, mark):
        self.mark = mark

    def __str__(self):
        return self.mark


class Board:
    """三目並べボード

    Attributes:
        size: ボードの1辺の大きさ
        cells: ボード上の各マス
        players: プレイヤー一覧
        player: 現在のプレイヤー
        puttables: 次にマークを置けるマス一覧
        is_slack: Slack 上でプレイする
    """

    def __init__(self):
        pass

    def setup(self, size=3, players=None):
        """ボードの初期化

        players は Player インスタンスの list です

        >>> player1 = Player('O')
        >>> player2 = Player('X')
        >>> board = Board()
        >>> board.setup(3, [player1, player2])

        Args:
            size: ボードの1辺の大きさ
            players: 参加するプレイヤー一覧
        """
        self.size = size
        self.cells = [[None] * self.size for _ in range(self.size)]
        self.players = players
        if self.players and len(self.players) != 2:
            raise ValueError('Set 2 players')
        self.is_slack = True
        self._player_idx = 0

    def get(self, x, y):
        """マスに置いてあるマークを読み取る

        Args:
            x: X座標
            y: Y座標
        """
        if self._is_xy_ok(x, y):
            return self.cells[y][x]

    def put(self, x, y):
        """マスにマークを置く

        self.player のマークを (x, y) 座標に置く

        Args:
            x: X座標
            y: Y座標
        """
        mark = self.player.mark
        if self._can_put(x, y):
            self.cells[y][x] = mark
            return mark

    def put_n(self, n):
        """マスにマークを置く

        self.player のマークをマス番号 n の場所に置く

        Args:
            n: マス番号
        """
        return self.put(*self._n2xy(n))

    def _n2xy(self, n):
        return n % self.size, n // self.size

    @property
    def player(self):
        """現在のプレイヤー"""
        return self.players[self._player_idx]

    @property
    def puttables(self):
        """次にマークを置けるマス一覧"""
        return [(x, y) for x in range(3) for y in range(3) if self._can_put(x, y)]

    def switch_player_turn(self):
        """次のプレイヤーに交代する"""
        self._player_idx += 1
        if self._player_idx >= len(self.players):
            self._player_idx = 0
        return self.player

    def _is_xy_ok(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def _can_put(self, x, y):
        return self._is_xy_ok(x, y) and self.get(x, y) is None

    def won(self):
        """現在のプレイヤーが勝ったかどうかを調べる

        Returns:
            True 勝ちだった場合。それ以外は False
        """
        mark = self.player.mark
        for x in range(self.size):
            if all(self.get(x, y) == mark for y in range(self.size)):
                return True
        for y in range(self.size):
            if all(self.get(x, y) == mark for x in range(self.size)):
                return True
        if all(self.get(i, i) == mark for i in range(self.size)):
            return True
        if all(
                self.get(x, y) == mark
                for x, y in zip(range(self.size), reversed(range(self.size)))):
            return True
        return False

    def is_end(self):
        """ゲームが引き分けで終わったかどうかを調べる

        Returns:
            True 引き分けだった場合。それ以外は False
        """
        for x in range(self.size):
            for y in range(self.size):
                if self.get(x, y) is None:
                    return False
        return True

    def format_board(self):
        """Slackに投稿するための文字列を作成する

        マークが置かれていないマスは番号に置き換わる
        例)
        0 1 2
        3 4 5
        6 7 8

        マークが置かれた場所はそのマークに置き換わる
        例)
        X 2 X
        4 O 6
        O 8 9

        Returns:
            str: ボードのマスを絵文字で置き換えた文字列
        """
        text = ''
        cell_number = 0
        for row in self.cells:
            for cell in row:
                if cell:
                    text += str(cell)
                elif self.is_slack:
                    try:
                        cell_char = NUMBER_ALPHA[cell_number]
                    except IndexError:
                        cell_char = 'hash'
                    text += f':{cell_char}:'
                else:
                    text += f' {cell_number}'
                cell_number += 1
            text += '\n'
        return text

    def __str__(self):
        """文字列に変換する"""
        return self.format_board()
