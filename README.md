# Hangman

[![Travis (.org)](https://img.shields.io/travis/svinkapeppa/hangman.svg)](https://travis-ci.org/svinkapeppa/hangman)
[![codecov](https://codecov.io/gh/svinkapeppa/hangman/branch/master/graph/badge.svg)](https://codecov.io/gh/svinkapeppa/hangman)

Console version of Hangman game

## Instalation

This is a Python 3.7 written game, so you need to have Python 3.7 installed. Visit [python.org](https://www.python.org/)
for further instructions.

### Requirements

All requirements are listed in [requirements.txt](requirements.txt). You can install them easily with pip
```
pip install -r requirements.txt
```

**N.B.**: Don't forget to active your virtual environment!

## Usage

You can play in your terminal. Extend [vocabulary](hangman/data/vocabulary.txt) to make your experience more interesting!

### Play

```
python -c "from hangman import Game; Game().play()"
```

### Tests

Module test and linting are combined

```
python -m pytest
```

## Contributing

Feel free to make pull requests and open issues. In urgent situations you can write [here](mailto:erubanenko@gmail.com)

## License

[MIT](LICENSE)
