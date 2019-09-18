import unittest

from hangman.game import Game


class GameTests(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_punish(self):
        self.game.punish()
        self.assertEqual(self.game.mistake_count, 1)

    def test_is_missed(self):
        self.game.word = 'word'
        self.assertTrue(self.game.is_missed('x'))

    def test_is_not_missed(self):
        self.game.word = 'word'
        self.assertFalse(self.game.is_missed('w'))

    def test_check_solved(self):
        self.game.word = 'word'
        self.game.pattern = 'word'
        self.game.check_solved()
        self.assertTrue(self.game.solved)


if __name__ == '__main__':
    unittest.main()
