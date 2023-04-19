#Creates the Map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

#Creates a nested list consisting of each row
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

#Prompt user to inut where they would like the treasure to be hidden
position = input("Where do you want to put the treasure? ")

#converts input value to int, subtracts 1, and assigns to variable
X_coordinate = int(position[0]) - 1
Y_coordinate = int(position[1]) - 1

#Changes the value in the current position to be X
map[Y_coordinate][X_coordinate] = "X"

#Prints final product   
print(f"{row1}\n{row2}\n{row3}")
