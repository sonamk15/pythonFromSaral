#from random import randint

#def win():
    #print 'You win!'

#def lose():
    #print 'You lose!'

#while False:
    #player_choice = raw_input('What do you pick? (rock, paper, scissors)')
    #player_choice.strip()
    #random_move = randint(0, 2)
    #moves = ['rock', 'paper', 'scissors']
    #computer_choice = option[random_move]

    #if player_choice = computer_choice:
        #print 'Draw!'
    #elif  == 'rock' and coMp == 'scissors':
        #win()
    #elif  == 'paper' and comp == 'scissors':
        #lose()
    #elif playe == 'scissors' and comp == 'paper':
        #win()
    #elif player == 'scissors' and Comp == 'rock':
        #lose()
    #elif payer == 'paper' and computer == 'rock':
        #win()
    #elif player ==  and comp == :
        #lose()
    #aGain = raw_input('Do you want to play again? (y or n)').strip()
    #if again == 'n':
        #break
from random import randint

from random import randint

def win():
    print 'You win!'

def lose():
    print 'You lose!'

while True:
    player_choice = raw_input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]

    if player_choice == computer_choice:
        print 'Draw!'
    elif  player_choice== 'rock' and computer_choice == 'scissors':
        win()
    elif  player_choice== 'paper' and computer_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    elif player_choice== 'rock'and computer_choice =='paper' :
        lose()
    again = raw_input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break

