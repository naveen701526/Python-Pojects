import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("Welcome to Rock Paper Scissors!!!.\npress 1 for rock\npress 2 for scissors\npress 3 for paper.\n"))

computer_choice = random.randint(1,3)

if user_choice == computer_choice:
  if user_choice == 1:
    print(rock)
    print('***************')
    print(rock)
    print('Well it\'s a draw')
  
  elif user_choice == 2:
    print(scissors)
    print('***************')
    print(scissors)
    print('Well it\'s a draw')
  
  else:
    print(paper)
    print('***************')
    print(paper)
    print('Well it\'s a draw')

elif user_choice == 1 and computer_choice == 2:
  print(rock)
  print('***************')
  print(scissors)
  print('You are the winner!! CONGRATULATIONS 🥳')

elif user_choice == 2 and computer_choice == 1:
  print(scissors)
  print('***************')
  print(rock)
  print('You are the loser!!')

elif user_choice == 1 and computer_choice == 3:
  print(rock)
  print('***************')
  print(paper)
  print('You are the loser!!')

elif user_choice == 3 and computer_choice == 1:
  print(paper)
  print('***************')
  print(rock)
  print('You are the winner!! CONGRATULATIONS 🥳')

elif user_choice == 2 and computer_choice == 3:
  print(scissors)
  print('***************')
  print(paper)
  print('You are the winner!! CONGRATULATIONS 🥳')

elif user_choice == 3 and computer_choice == 2:
  print(paper)
  print('***************')
  print(scissors)
  print('You are the winner!! CONGRATULATIONS 🥳')



else:
  print('WRONG INPUT TRY AGAIN!!')