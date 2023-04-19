#Greeting message to greet the user
print("Welcome to Treasure Island. Your mission is to find the treasure.")

#prompts the user to input a choice, makes it lowercase, and assigns to a variable
first_choice = input("Would you like to go left or right? ").lower()


#multiple conditional statments, the logic or "Brains" of the game.
if (first_choice == "right"):
    print("Oh No! You've run into a gang of pirates and they've taken you hostage. Game over.")
elif (first_choice == "left"):
    second_choice = input("Would you like to swim or wait? ").lower()
    if second_choice == "swim":
        print("Should've invested more in swimming lessons. You sink like a rock and drown. Game over.")
    elif second_choice == "wait":
        third_choice = input("Which door would you like to check? blue, yellow, or red? ").lower()
        if third_choice == "red":
            print("The Ender Dragon is behind this door and cooks you. Game Over.")
        elif third_choice == "blue":
            print("Medusa is behind this door and turns you to stone. Game Over.")
        elif third_choice == "yellow":
            print("You've found the treasure! Congratulations!")
        else:
            print("That's not an option. Game over.")
    else:
        print("That's not an option. Game over.")
else:
    print("That's not an option. Game over.")