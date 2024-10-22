#A hangman game: the computer picks a random word and the user has to guess what it is

import random
from words import words
import string
from hangman_visual import lives_visual_dict



def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():

    lives = 7
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0 and lives > 0 :

        print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("\nThe current word is: ", ' '.join(word_list))
        

        user_letter = input("\nGuess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives = lives-1
                print('\nLetter is not in the word')
        elif user_letter in used_letters:
            print("\nYou have already used that charachter. Please try again.")
        else:
            print("\nInvalid character. Please try again.")
    if lives == 0:
        print("\nSorry, you have died. The word was", word)
    else:
        print("\nYay, you won!! You guessed the word", word, 'in', 10-lives, "tries!")


hangman()


