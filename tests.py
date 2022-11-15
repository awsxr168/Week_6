import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.Board.get_winner(board), 'X')

    def test_move_board(self, row, col):
        self.assertEqual(logic.Board.move_board(), '2', '2')

    def test_mode(self):
        input = '1'
        self.assertEqual(logic.Game.mode(input), '1')

    def test_run(self):
        logic.Game.winner == None
        self.assertEqual(logic.Game.run())

    def test_change_player(self):
        logic.Game.current_player = 'playerX'
        self.assertEqual(logic.Game.change_player(), 'playerX')


if __name__ == '__main__':
    unittest.main()
