import random

word_list = ['Apple', 'Banana', 'Pear', 'Kiwi', 'Lemon']
secret_word = random.choice(word_list).lower()
print(secret_word)

while True:
    guess = input('Please enter your guess:').lower()
    if guess.isalpha():
        print('Good guess!')
        if guess in secret_word:
            print(f'{guess} is in the secret word.')
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
        break
    else:
        print('Invalid letter. Please enter a single alphabetical character.')
