import os, platform, time


def clear():
    if 'linux' in platform.system().lower():
        os.system('clear')
    elif 'windows' in platform.system().lower():
        os.system('cls')
def number_game(value, number):
    '''Starts the game of Guessing the right number.'''
    clear()
    chances = value
    i = 0
    while i < value:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess > number:
            print("Too high.")
            if not i == value - 1:
                print("Guess again.")
                time.sleep(2)
                clear()
        elif guess < number:
            print("Too low.")
            if not i == value - 1:
                print("Guess again")
                time.sleep(2)
                clear()
        chances -= 1
        i+=1
    if i >= value:
        print("You've run out of guesses, you lose.")