"""
In this project, we'll build Rock-Paper-Scissors!

The program should do the following:

Prompt the user to select either Rock, Paper, or Scissors
Instruct the computer to randomly select either Rock, Paper, or Scissors
Compare the user's choice and the computer's choice
Determine a winner (the user or the computer)
Inform the user who the winner is

Let's begin!
"""

from random import randint
from time import sleep

options = ["ROCK", "PAPER", "SCISSORS"]
LOSS_MESSAGE = "You Lost!"
WIN_MESSAGE = "You Won!"
TIE_MESSAGE = "It is a Tie!"


def decide_winner(user_choice, computer_choice):
    print "You selected: %s" % user_choice
    print "Computer selected: %s" % computer_choice
    sleep(1)
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print TIE_MESSAGE
    elif user_choice_index == 0 and computer_choice_index == 2:
        print WIN_MESSAGE
    elif user_choice_index == 1 and computer_choice_index == 0:
        print WIN_MESSAGE
    elif user_choice_index == 2 and computer_choice_index == 1:
        print WIN_MESSAGE
    elif user_choice_index > 2:
        print "An invalid option was selected!"
        return
    else:
        print LOSS_MESSAGE


def play_RPS():
    user_choice = raw_input("Rock, Paper or Scissors? Type: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, len(options) - 1)]
    decide_winner(user_choice, computer_choice)


play_RPS()





