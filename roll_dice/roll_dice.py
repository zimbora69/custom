'''
Wanna play a game?
In this project, the bot and the user are asked to guess a number.
Based on the user and bot's guess, the program should determine a winner.
Two dices are rolled, the user who get's closer to the total value of the dices wins!
'''
from random import randint
from time import sleep


def get_user_guess():
    user_guess = int(raw_input("Guess a number: "))
    return user_guess


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    b = randint(1,max_val)
    print "The maximum possible value is: " + str(max_val)
    sleep(1)
    user_guess = get_user_guess()
    print "My Guess is " + str(b)
    if user_guess > max_val:
        print "No guessing higher than the maximum possible value!"
        return
    else:
        print "Rolling dices..."
        sleep(2)
        print "The first value is: %d" % first_roll
        sleep(1)
        print "The second value is: %d" % second_roll
        sleep(1)
        total_roll = first_roll + second_roll
        print "The total value is: %d" % total_roll
        if (abs(user_guess - total_roll)) < (abs(b - total_roll)):
            print "You won!"
            return
        elif (abs(user_guess - total_roll)) == (abs(b - total_roll)):
            print "We are tied!"
            return
        else:
            print 'You lost, try again.'
            return
a='yes'
while(a=='yes'):
    roll_dice(6)
    a = raw_input("Retry? Type yes or no ")
