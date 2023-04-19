row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
X_coordinate = int(position[0]) - 1
Y_coordinate = int(position[1]) - 1

print(X_coordinate)
print(Y_coordinate)

map[Y_coordinate][X_coordinate] = "X"


print(f"{row1}\n{row2}\n{row3}")
