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

#Prompts the user to input a choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

#Randomizes the computer's choice between 0 and 2
computer_choice = random.randint(0,2)

#Creates a list to hold the emojis
emoji_list=[rock, paper, scissors]

#prints the user and computer selected emojis respectively
if user_choice >= 0 and user_choice <= 2:
    print(emoji_list[user_choice])
print("Computer chose: ", emoji_list[computer_choice])


#logic to determine who wins the game
if user_choice == 0:
    if computer_choice == 0:
        print("Draw")
    elif computer_choice == 1:
        print("You lose")
    else:
        print("You win")

if user_choice == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 1:
        print("Draw")
    else:
        print("You lose")

if user_choice == 2:
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
    else:
        print("Draw")

#added a bit of error handling in case the user doesn't follow the rules
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number, you lose")