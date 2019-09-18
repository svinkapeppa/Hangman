from pathlib import Path
from random import randint


class Game:
    solved = False
    word = ''
    pattern = ''
    mistake_count = 0
    max_mistake_count = 5
    vocabulary_path = 'vocabulary.txt'
    directory_path = 'hangman/data/'

    def __init__(self):
        pass

    @staticmethod
    def congratulate():
        print('\nYou won!')

    @staticmethod
    def scold():
        print('\nYou lost!')

    @staticmethod
    def greet():
        print('\nGuess a letter:')

    def generate_word(self):
        path = Path(self.directory_path) / self.vocabulary_path
        words = [line.rstrip('\n') for line in open(path)]
        self.word = words[randint(0, len(words))]
        self.pattern = '*' * len(self.word)

    def is_missed(self, letter):
        return letter.lower() not in self.word.lower()

    def punish(self):
        self.mistake_count += 1
        print('Missed, mistake {} out of {}'.format(self.mistake_count, self.max_mistake_count))

    def reward(self, letter):
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
        print('\nThe word: {}'.format(self.pattern))

    def check_solved(self):
        self.solved = self.pattern.lower() == self.word.lower()

    def play(self):
        self.generate_word()

        while self.mistake_count < self.max_mistake_count:
            if self.solved:
                self.congratulate()
                return
            else:
                self.greet()
                letter = input()

                if self.is_missed(letter):
                    self.punish()
                else:
                    self.reward(letter)
                    self.check_solved()

                self.remind()

        self.scold()
        return
