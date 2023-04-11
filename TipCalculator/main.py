#prompt the user for the bills total amount
total=float(input("What was the total bill? "))


#prompt user for tip amount
tip=float(input("What percentage tip would you like to give? 10, 12, or 15? "))


#calculate the total after the tip is applied. 
total_after_tip = total * (tip/100 + 1)

#prompt the user to input number of friends splitting the bill
friends=float(input("How many people to split the bill? "))

#calculate the final after the the total and friends are input
final=total_after_tip/friends

#print final and round to two decimal places. 
print(round(final, 2))


