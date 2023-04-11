height = int(input("How tall are you in CM? "))

if height > 120:
    print("Have fun!")
    age=int(input("How old are you? "))
    if age < 12:
        print("You only owe $5")
    elif age >= 12 & age <= 18:
        print("You owe $7")
    else:
        print("You owe $12")
else: 
    print("Sorry, you're to short to ride the roller coaster :(")