import random

word_list = ['Apple', 'Banana', 'Pear', 'Kiwi', 'Lemon']
print(random.choice(word_list))


while 1 == 1:
    guess = input('Please enter your guess:')
    if len(guess) == 1:
        print('Good guess!')
        break
    else:
        print('Oops! Thats not a valid input.')
