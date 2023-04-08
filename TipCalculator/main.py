#prompt the user for the bills total amount
total=input("What was the total bill? ")

#convert total to floating point value
new_total=float(total)

#prompt user for tip amount
tip=input("What percentage tip would you like to give? 10, 12, or 15? ")
#convert tip to float
new_tip=float(tip)

#calculate the total after the tip is applied. 
total_after_tip = new_total * (new_tip/100 + 1)

#calculate final after the bill and tip are split
friends=input("How many people to split the bill? ")


new_friends=float(friends)

final=total_after_tip/new_friends

print(round(final, 3))

