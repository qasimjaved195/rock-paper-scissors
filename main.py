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


print("Welcome to the Rock Paper Scissors game!")

user_choice = int(input("Write 0 for Rock, 1 for Paper and 2 for Scissors. "))

choices = [rock, paper, scissors]

print(f"You selected \n{choices[user_choice]}")

computer_choice = random.randint(0,2)

print(f"Computer selected \n{choices[computer_choice]}")

str_win = "Congratulations, you win."
str_lose = "You lose."

user_win = 1

if user_choice == 0 and computer_choice == 1:
    print(str_lose)
elif user_choice == 0 and computer_choice == 2:
    print(str_win)
elif user_choice == 1 and computer_choice == 0:
    print(str_win)
elif user_choice == 1 and computer_choice == 2:
    print(str_lose)
elif user_choice == 2 and computer_choice == 0:
    print(str_lose)
elif user_choice == 2 and computer_choice == 1:
    print(str_win)
elif user_choice == computer_choice:
    print("It's a draw.")
else:
    print("You entered invalid number.")