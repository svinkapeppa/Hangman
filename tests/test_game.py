from hangman.game import Game

"""
Tests
"""


def test_punish():
    """
    Tests that `punish()` actually increases the counter
    :return:
    """
    game = Game()
    game.punish()
    assert game.mistake_count == 1


def test_is_missed():
    """
    Tests that wrong letter isn't found in the word
    :return:
    """
    game = Game()
    game.word = 'word'
    assert game.is_missed('x') is True


def test_is_not_missed():
    """
    Tests that correct letter is found in the word
    :return:
    """
    game = Game()
    game.word = 'word'
    assert game.is_missed('w') is False


def test_check_solved():
    """
    Tests that positive end-game condition is tracked
    :return:
    """
    game = Game()
    game.word = 'word'
    game.pattern = 'word'
    game.check_solved()
    assert game.solved is True
