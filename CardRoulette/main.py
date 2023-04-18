import random

#Prompts the user for the names of the attendees and places them into a list
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#This gets the length of the list
length_of_list = len(names)

#This will get the integer of the person paying by randomization
paying_int = random.randint(0, length_of_list-1)

#This line takes the integer from above and assigns correlating string to the who's_paying variable
whos_paying = names[paying_int]

print(f"{whos_paying} is going to buy the meal today!")

