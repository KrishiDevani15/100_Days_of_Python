import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(
"""

game_img = [rock, paper,scissors]

user_name = input("Enter your name:\n >> ")
user_choice = int(input('What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors:\n >> '))

if 0 <= user_choice <= 2:
    print(f"{user_name} choose: ")
    print(game_img[user_choice])

computer_choice = random.randint(0,2)
print("Computer choose: ")
print(game_img[computer_choice])

if (user_choice < 0 or user_choice >= 3):
    print("You typed and invalid number. You lose !")

elif user_choice == 0 and computer_choice == 2:
    # user --> rock(0) and computer --> Scissors(2)
    print(f"{user_name} wins")

elif user_choice == 2 and computer_choice == 0:
    # user --> Scissors and computer --> rock
    print("You lose")

elif (user_choice < computer_choice):
    # user --> rock(0) and computer --> paper(1)
    # user --> paper(1) and computer --> Scissors(2)
    print("you lose")

elif (user_choice > computer_choice):
    # user --> paper(1) and computer --> rock(0)
    # user --> Scissors(2) and computer --> paper(1)
    print(f"{user_name} wins")

elif (user_choice == computer_choice):
    print("It's Tie")








