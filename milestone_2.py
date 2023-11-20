import random

word_list = ['Apple', 'Banana', 'Pear', 'Kiwi', 'Lemon']
secret_word = random.choice(word_list).lower()
print(secret_word)




def check_guess(guess):
    if guess in secret_word:
        print(f'{guess} is in the secret word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

    return 

def ask_for_input():
    while True:
        guess = input('Please enter your guess:').lower()
        if guess.isalpha():
            print('Good guess!')
            check_guess(guess)
            break
        else:
            print('Invalid letter. Please enter a single alphabetical character.')
    
    return guess

ask_for_input()
