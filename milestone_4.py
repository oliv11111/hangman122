import random
class Hangman:
    def __init__(self, word_list, num_lives=5, list_of_guesses=None):
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
    

        

    def ask_for_input(self):
        while True:
            guess = input('Please enter your guess:')
            if guess.isalpha() == False:
                print('Invalid letter. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter.')
            else: 
                self.check_guess(guess)
    



game1 = Hangman(['Apple', 'Banana', 'Pear', 'Kiwi', 'Lemon'])
print(game1.word_list)
print(game1.num_lives)
print(game1.word)
print(game1.word_guessed)
print(game1.num_letters)
print(game1.list_of_guesses)

game1.ask_for_input()