"""Hangman game"""
import string
from pathlib import Path
from random import randint


class Game:
    """
    Class, that encapsulates game itself
    """
    solved = False
    word = ''
    pattern = ''
    mistake_count = 0
    max_mistake_count = 5
    vocabulary_path = 'vocabulary.txt'
    directory_path = 'hangman/data/'

    @staticmethod
    def congratulate():
        """
        End-game congratulation in case of winning
        :return:
        """
        print('\nYou won!')

    @staticmethod
    def scold():
        """
        Eng-game congratulation in case of loosing
        :return:
        """
        print('\nYou lost!')

    @staticmethod
    def greet():
        """
        Greet user each round
        :return:
        """
        print('\nGuess a letter:')

    @staticmethod
    def is_letter_valid(letter):
        """
        Checks for valid input
        :param letter: character, typed by user
        :return: True, if it's an english character; False otherwise
        """
        if letter == '':
            return False
        return letter.lower() in string.ascii_lowercase

    @staticmethod
    def warn():
        """
        Warns user, because he/she typed something bad
        :return:
        """
        print('Stop cheating! Write valid english letters!')

    def generate_word(self):
        """
        Generate word and blank pattern
        :return:
        """
        path = Path(self.directory_path) / self.vocabulary_path
        words = [line.rstrip('\n') for line in open(path)]
        self.word = words[randint(0, len(words))]
        self.pattern = '*' * len(self.word)

    def is_missed(self, letter):
        """
        Check if provided letter is in the word
        :param letter:
        :return:
        """
        return letter.lower() not in self.word.lower()

    def punish(self):
        """
        Punish user for mistakes
        :return:
        """
        self.mistake_count += 1
        template = 'Missed, mistake {} out of {}'
        print(template.format(self.mistake_count, self.max_mistake_count))

    def reward(self, letter):
        """
        Reward user for correct letters
        :param letter: character, typed by user
        :return:
        """
        pattern = ''
        for idx, char in enumerate(self.pattern):
            if char != '*':
                pattern += char
            elif self.word[idx].lower() == letter.lower():
                pattern += self.word[idx]
            else:
                pattern += '*'
        self.pattern = pattern
        print('Hit!')

    def remind(self):
        """
        Show pattern to the user
        :return:
        """
        print('\nThe word: {}'.format(self.pattern))

    def check_solved(self):
        """
        Positive end-game condition
        :return:
        """
        self.solved = self.pattern.lower() == self.word.lower()

    def play(self):
        """
        Game itself
        :return:
        """
        self.generate_word()

        while self.mistake_count < self.max_mistake_count:
            if self.solved:
                self.congratulate()
                return

            self.greet()
            letter = input()
            if not self.is_letter_valid(letter):
                self.warn()
                continue

            if self.is_missed(letter):
                self.punish()
            else:
                self.reward(letter)
                self.check_solved()

            self.remind()

        self.scold()
        return
