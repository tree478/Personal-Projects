from turtle import *
import turtle
from random import *

t = turtle.Turtle()

#Choose a number for the user to guess

number = randint(1, 100)
print(number)

wn = turtle.Screen()

user_input = turtle.numinput("Guessing Game", "Guess a number between 1 and 100:")      #Get input from the user
score = 0       #Keeping track of score - start with 0

#In this section, python will compare the user input to the number until they match. 
#If the user input is greater than the number, python will execute the code under the if statement: 
# say that it is too high and that the user should guess again
#If the input is less than the number, python will execute the code under the elif statement: 
# say that the number is too low and that the user should guess again

while (user_input != number):
    if (user_input > number):
        user_input = user_input = turtle.numinput("Guessing Game", "Your number was too high. Guess again:")
        #Adds one point to the scoreboard
        score = score + 1
    elif (user_input < number):
        user_input = user_input = turtle.numinput("Guessing Game", "Your number was too low. Guess again:")
        score = score + 1

#When the user guesses the number, pyton runs this code. Using turtle, it will print that the user has guessed the right number, 
# and the number of tries to took them. Then it will ask the user what they want to see as a prize, 
# and then clear the screen to draw that prize.

if (user_input == number):
    turtle.pencolor("teal")
    words = 'You won! You guessed the correct number! It took you', score, 'tries.'
    turtle.write(words, align="right", font=("Comic Sans MS", 25, "bold"))
    prize = turtle.textinput("Chose your prize","What would you like to see as a prize?(spiral/shape)")
    wn.clear()

#Executes different code depending on what the user inputs
    if (prize == "spiral"):
        #Setting the pen
        t.speed(0)
        t.width(4)
        sides = turtle.numinput("Sides", "How many sides do you want your spiral to have?") #Asks how many sides the user wants
        sides = int(sides)  #Makes the input an integer
        degree = (360 / sides) - 3  #Calculates degrees the turtle turns when drawing spiral
        status = "y"    #Beginning conditional for while loop
        colors = []     #Empty list to add input to
        while status == "y":
            #While the user still wants to add colors, asks the user what color they want to add
            color = turtle.textinput("Choose color", "What color do you want to add?(Please don't add very exotic colors, python doesn't understand them)")
            colors.append(color)       #Adds that color to the color list created earlier
            status = turtle.textinput("Add color", "Do you want to add a color?(y/n)")
            #If user says they don't want to add another color, exits while loop

        #Draws spiral
        for m in range(1000):
            t.pencolor(colors[m%len(colors)])
            t.forward(m * 2)
            t.left(degree)

    if (prize == "shape"):

        t.speed(0)
        t.width(4)

        sides = turtle.numinput("Sides", "How many sides do you want your shape to have?")
        sides = int(sides)
        degree = (360 / sides)      #Code is basically the same as above, 
                                    # just different angle which makes an enless shape instead of a spiral

        status = "y"
        colors = []
        while status == "y":
            color = turtle.textinput("Choose color", "What color do you want to add?(Please don't add very exotic colors, python doesn't understand them)")
            colors.append(color)
            status = turtle.textinput("Add color", "Do you want to add a color?(y/n)")

        for m in range(1000):
            t.pencolor(colors[m%len(colors)])
            t.forward(m * 3)
            t.left(degree)

wn.mainloop()