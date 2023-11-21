import random

WORD_LIST = ['Apple', 'Banana', 'Pear', 'Kiwi', 'Lemon']
NUM_LIVES = 5

class Hangman:
    def __init__(self, word_list, num_lives, list_of_guesses=None):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = list_of_guesses or []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print(f'Good guess! {guess} is in the word.')
            for i, letter in enumerate(self.word):
                if letter.lower() == guess:
                    self.word_guessed[i] = letter
            self.num_letters = self.num_letters - 1
            

        else:
            self.num_lives = self.num_lives - 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have, {self.num_lives} lives left.')
    

        

    def ask_for_input(self):
        while True:
            guess = input('Please enter your guess:')
            if guess.isalpha() == False:
                print('Invalid letter. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter.')
            else: 
                self.check_guess(guess)
                break
    




def play_game(WORD_LIST, NUM_LIVES):
    game = Hangman(WORD_LIST, NUM_LIVES)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            return False
        elif game.num_letters > 0:
            game.ask_for_input()
        else: 
            print('Congratulations, you have won the game!')
            return False

play_game(WORD_LIST, NUM_LIVES)
        