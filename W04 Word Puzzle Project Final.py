'''Random library with choise function used to generate different secret words
play again option added. the use of a list and function also included'''
import random

play_again = 'yes'

def check_word():
    guessed_word = ''
    count = 0

    while guessed_word.lower() != secret_word:
        guessed_word = input('What is your guess? ')
        guessed_word = guessed_word.lower() 
        count = count + 1

        if len(guessed_word) == len(secret_word):
            if guessed_word == secret_word:
                print('Congratulations! You guessed it!')
                print(f'It took you {count} guesses.')
            else:
                print('Your hint is: ', end='')
                for char, word in zip(secret_word, guessed_word):
                    if word in secret_word and word in char:
                        print(word.upper(), end='')
                    elif word in secret_word:
                        print(word.lower(), end='')
                    else:
                        print('_', end='')
                print()
        else:
            print('Sorry, the guess must have the same number of letters as the secret word.\n')

while play_again == 'yes':
    secret_words = ['nephi', 'jacob', 'enos', 'jarom', 'omni', 'mormon', 'mosiah', 'alma', 'helaman', 'ether', 'moroni']
    secret_word = random.choice(secret_words)

    print("Welcome to the Book of Mormon prophet names guessing game!\n")

    hint =''
    for letter in secret_word:
        hint = hint + '_ '   
    print(f'Your hint is: {hint}')                
    check_word()
    
    play_again = input('\nWould you like to play again? yes/no ')