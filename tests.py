import unittest
from cli import TicTacToeGame
from logic import check_winner, get_empty_board
from bot import Bot
from unittest.mock import patch
import io

class TestTicTacToe(unittest.TestCase):

    def test_game_initialization(self):
        game = TicTacToeGame(mode="single")
        self.assertEqual(game.current_player, "X")
        self.assertEqual(game.board, get_empty_board())
        self.assertIsNone(game.winner)
        self.assertEqual(game.mode, "single")

    def test_switch_player(self):
        self.assertEqual(TicTacToeGame(mode="single").current_player, "X")
        self.assertEqual(TicTacToeGame(mode="two").current_player, "X")

    def test_check_winner_rows(self):
        board = [
            ['X', 'X', 'X'],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(check_winner(board), 'X')

    def test_check_winner_columns(self):
        board = [
            ['X', None, None],
            ['X', None, None],
            ['X', None, None],
        ]
        self.assertEqual(check_winner(board), 'X')

    def test_check_winner_columns_other_play(self):
        board = [
            [None, None, 'O'],
            [None, None, 'O'],
            [None, None, 'O'],
        ]
        self.assertEqual(check_winner(board), 'O')

    def test_check_winner_left_diagonals(self):
        board = [
            ['X', None, None],
            [None, 'X', None],
            [None, None, 'X'],
        ]
        self.assertEqual(check_winner(board), 'X')

    def test_check_winner_diagonals(self):
        board = [
            [None, None, 'X'],
            [None, 'X', None],
            ['X', None, None],
        ]
        self.assertEqual(check_winner(board), 'X')

    def test_check_draw(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertEqual(check_winner(board), 'Draw')
    
    def test_check_none(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(check_winner(board), None)

    def test_play_game(self):
        with patch('builtins.input', side_effect=['single', '0,0', '0,1', '1,1', '1,0', '2,2']):
            game = TicTacToeGame(mode="single")
            game.play_game()
            self.assertIsNotNone(game.winner)

    def test_get_bot_move(self):
        bot = Bot()
        board = [
            ['X', 'O', 'X'],
            ['O', None, None],
            [None, None, 'X'],
        ]
        move = bot.get_bot_move(board)
        self.assertIn(move, [(1, 1), (1, 2), (2, 0), (2, 1)])

if __name__ == '__main__':
    unittest.main()
