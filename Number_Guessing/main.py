from art import logo
from random import randint

from number_game import number_game






print(logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
number = randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'hard':
    number_game(5, number)
elif difficulty == 'easy':
    number_game(10, number)
    
