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
game_images = [rock, paper, scissors]
print("welcome to the rock paper scissors game")
choices = ["rock", "paper", "scissors"]
user_choices = int(input("what would you like to choose, 0 for rock, 1 for paper, 2 for scissors: "))
if user_choices >= 3 or user_choices < 0:
    print("You typed an invalid number. You lose!")
else:
   print("user choose: ", choices[user_choices])
   print(game_images[user_choices])
   computer_choice = random.randint(0, 2)
   print("Computer choose:", choices[computer_choice])
   print(game_images[computer_choice])
   if user_choices == computer_choice:
    print("it's a tie")
   elif user_choices == 0 and computer_choice == 2:
    print("You win!")
   elif user_choices == 1 and computer_choice == 0:
    print("You win!")
   elif user_choices == 2 and computer_choice == 1:
    print("You win!")
   else:
    print("You lose!")


