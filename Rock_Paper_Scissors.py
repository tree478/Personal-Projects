import random

choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
player = 'play'

print('Welcome to the battle of rock paper scissors! We will now determine who is the champion player: you or the computer!\n')

while player != 'quit':
    player = input('Pick one: rock, paper, or scissors(or quit). Rock crushes scissors, scissors cut paper, and paper wraps rock.')
    computer = random.choice(choices)
    if player == 'rock':
        print('You chose', player, 'and the computer chose', computer)
        if computer == 'paper':
            computer_score == computer_score + 1
            print('The computer chose paper. Sorry, you lose.')
        elif computer == player:
            print('It was a tie!')
        else:
            player_score = player_score + 1
            print("The computer chose", computer, '!! You win!')
    if player == 'paper':
        print('You chose', player, 'and the computer chose', computer)
        if computer == 'scissors':
            computer_score == computer_score + 1
            print('The computer chose scissors. Sorry, you lose.')
        elif computer == player:
            print('It was a tie!')
        else:
            player_score = player_score + 1
            print('The computer chose', computer, '!! You win!')
    if player == 'scissors':
        print('You chose', player, 'and the computer chose', computer)
        if computer == 'rock':
            computer_score == computer_score + 1
            print('The computer chose rock. Sorry, you lose.')
        elif computer == player:
            print('It was a tie!')
        else:
            player_score = player_score + 1
            print("The computer chose", computer, '!! You win!')

if player == 'quit':
    print('The rock paper scissors battle is over! The final standings are: \nYou:', player_score, '\nComputer:', computer_score)
    if player_score > computer_score:
        print("Congratulations!!You won the battle! You are now the ultimate rock paper scissors champion!")
    if player_score < computer_score:
        print('I am so sorry! The computer won! I guess you just have to keep trying if you want to be the champion!')
    if player_score == computer_score:
        print("It was a tie! I guess both of you are evenly matched!")



