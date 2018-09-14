# -*- coding: utf-8 -*-
import unittest

from samplebot.plugins.libs.tictactoe import Board, Player


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.setup(3, [Player('X'), Player('O')])

    def test_board_get(self):
        self.board.cells = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(self.board.get(0, 0), 1)
        self.assertEqual(self.board.get(0, 1), 4)
        self.assertEqual(self.board.get(1, 1), 5)
        self.assertEqual(self.board.get(1, 0), 2)
        self.assertEqual(self.board.get(4, 0), None)
        self.assertEqual(self.board.get(0, 4), None)

    def test_board_put(self):
        self.assertEqual(self.board.put(0, 0), 'X')
        self.assertEqual(self.board.get(0, 0), 'X')
        self.assertEqual(self.board.put(0, 1), 'X')
        self.assertEqual(self.board.get(0, 0), 'X')
        self.assertEqual(self.board.put(1, 0), 'X')
        self.assertEqual(self.board.get(1, 0), 'X')
        self.assertEqual(self.board.put(4, 0), None)
        self.assertEqual(self.board.put(0, 4), None)

    def test_switch_player_turn(self):
        self.assertEqual(self.board.player.mark, 'X')
        self.board.switch_player_turn()
        self.assertEqual(self.board.player.mark, 'O')
        self.board.switch_player_turn()
        self.assertEqual(self.board.player.mark, 'X')

    def test_horizontal_won(self):
        self.board.cells[0] = ['X', 'X', 'X']
        self.assertTrue(self.board.won())

    def test_vertical_won(self):
        self.board.cells = [
            ['X', None, None],
            ['X', None, None],
            ['X', None, None],
        ]
        self.assertTrue(self.board.won())

    def test_diagonal_won(self):
        self.board.cells = [
            ['X', None, None],
            [None, 'X', None],
            [None, None, 'X'],
        ]
        self.assertTrue(self.board.won())
        self.board.cells = [
            [None, None, 'X'],
            [None, 'X', None],
            ['X', None, None],
        ]
        self.assertTrue(self.board.won())

    def test_is_end(self):
        self.assertFalse(self.board.is_end())
        self.board.cells = [
            ['O', 'O', 'X'],
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
        ]
        self.assertTrue(self.board.is_end())

    def test_n2xy(self):
        self.board.cells = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        for n in range(9):
            self.assertEqual(self.board.get(*self.board._n2xy(n)), n + 1)


if __name__ == '__main__':
    unittest.main()
