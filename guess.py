'''
The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
    within 10 of the number, return "WARM!"
    further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
    closer to the number than the previous guess return "WARMER!"
    farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

'''

from random import randint

x = randint(1, 100)
turn = 0

while True:
    y = int(input('Enter number: '))
    turn += 1
    if 1 > y > 100:
        print('OUT OF BOUNDS')
    elif y == x:
        print('CORRECT! Number of guesses: ', turn)
        break
    elif turn == 1 and abs(x - y) < 10:
        print('WARM!')
        prev = y
    elif turn == 1 and abs(x - y) > 10:
        print('COLD!')
        prev = y
    elif turn > 1 and y < prev:
        print('WARMER!')
        prev = y
    elif turn > 1 and y > prev:
        print('COLDER!')
        prev = y
