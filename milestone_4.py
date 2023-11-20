import random
class Hangman:
    def __init__(self, word_list, num_lives=5, list_of_guesses=None):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = list_of_guesses or []

        


game1 = Hangman(['Apple', 'Banana', 'Pear', 'Kiwi', 'Lemon'])
print(game1.word_list)
print(game1.num_lives)
print(game1.word)
print(game1.word_guessed)
print(game1.num_letters)
print(game1.list_of_guesses)