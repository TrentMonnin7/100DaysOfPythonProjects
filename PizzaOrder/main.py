#setup problem by defining variables
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
running_total=0

if size == 'S':
    running_total=15
    if add_pepperoni == 'Y':
        running_total += 2
    if extra_cheese == 'Y':
        running_total += 1
elif size == 'M':
    running_total=20
    if add_pepperoni == 'Y':
        running_total += 3
    if extra_cheese == 'Y':
        running_total += 1
else:
    running_total=25
    if add_pepperoni == 'Y':
        running_total += 3
    if extra_cheese == 'Y':
        running_total += 1

print(F"Your final bill is: ${running_total}")