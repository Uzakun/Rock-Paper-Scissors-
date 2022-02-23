              #Method1

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

T = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for scissors.\n"))

if T == 0:
  print(rock)
elif T == 1:
  print(paper)
elif T == 2:
  print(scissors)  

print("Computer Side:")  

computer = random.randint(0, 2)

if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)  

if T == 0 and computer == 0:
  print("Draw!")
elif T == 1 and computer == 1:
  print("Draw!")
if T == 2 and computer == 2:
  print("Draw!")  
if T == 0 and computer == 1:
  print("You Lose!")
if T == 1 and computer == 2:
  print("You Lose!") 
elif T == 2 and computer == 0:
  print("You Lose!")   
if T == 1 and computer == 0:
  print("You Win! ^^")
if T == 2 and computer == 1:
  print("You Win! ^^") 
elif T == 0 and computer == 2:
  print("You Win! ^^")
 

          #Method2(More Concised)

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")






