import random

#prompts the user to guess between Heads and Tails
guess=input("Heads or Tails? ")

#Capitalizes the first letter of the user's guess
guess_cap = guess.capitalize()


random_number=random.randint(0,1)

if random_number == 1:
    print("The coin flip is Heads")
else:
    print("The coin flip is Tails")
