from hangman.game import Game


def test_punish():
    game = Game()
    game.punish()
    assert game.mistake_count == 1


def test_is_missed():
    game = Game()
    game.word = 'word'
    assert game.is_missed('x') is True


def test_is_not_missed():
    game = Game()
    game.word = 'word'
    assert game.is_missed('w') is False


def test_check_solved():
    game = Game()
    game.word = 'word'
    game.pattern = 'word'
    game.check_solved()
    assert game.solved is True
