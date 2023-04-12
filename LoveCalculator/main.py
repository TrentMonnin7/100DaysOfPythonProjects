print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Combine the names and put in lower case
combined_names=name1.lower() + name2.lower()

#Count the amount of times the letters "TRUE" appear in the names and add together. Then the value is converted to a string
count_of_true=str(combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e'))



#Count the amount of times the letters "LOVE" appear in the names and add together. Then the value is converted to a string
count_of_love=str(combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e'))

#combines the two to make a total love score and converts back to integer
total_love_score = int(count_of_true + count_of_love)


#Use conditionals to print out the desired message with score
if total_love_score < 10 or total_love_score > 90:
    print(f"Your score is {total_love_score}, you go together like coke and mentos.")
elif total_love_score >= 40 and total_love_score <= 50:
    print(f"Your score is {total_love_score}, you are alright together.")
else:
    print(f"Your score is {total_love_score}.")
