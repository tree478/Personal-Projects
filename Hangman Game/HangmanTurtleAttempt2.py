#An attempt to enhance previously created hangman game by adding more visuals and user interactivity

import random
from words import words
import string
from hangman_visual import lives_visual_dict
import turtle


t = turtle.Turtle()
t.hideturtle()
turtle.bgcolor("black")
t.pencolor("white")
t.width(3)

def goto(x,y):

    t.penup()
    t.setposition(x,y)
    t.pendown()

def drawhangman():

    t.penup()
    t.setpos(70,70)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(70)
    t.backward(140)

drawhangman()

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

word = get_valid_word(words)

word_letters = list(word)
number = len(word)
distance = 400/number
print(word)


def draw_blank_lines():
    for m in range (number):
        t.forward(18)
        t.penup()
        t.forward(8)
        t.pendown()

goto(-245,-105)
draw_blank_lines()


def hangman():

    lives = 7
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0 and lives > 0 :

        print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '   ' for letter in word]
        def add_letters():
            for i in range(number):
                t.write((word_list[i]), align="left")
                t.penup()
                t.forward(25)
                t.pendown()
        print(lives_visual_dict[lives])
        print("\nThe current word is: ", ' '.join(word_list))
        goto(-233,-102)
        t.write(add_letters)
        

        user_letter = turtle.textinput("Guess","Guess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            goto(-295,235)
            t.write(f'You have used these letters: {used_letters}')
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

wn = turtle.Screen()
wn.mainloop()