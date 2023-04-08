#Prompt the user to enter their name to make a personalized welcome message
name = input("What is your name?: ")

#Prints a welcome message for the user
print("Hello " + name + ", welcome to the band name generator!")

#Prompts the user for the name of their city
city = input("What city did you grow up in?: ")

#Prompts the user for the name of their pet
petName = input("What is the name of your pet?: ")

#Combines the user inputted city name with the pet name
bandName = city+ " " + petName

#Prints the output to the user
print("The name of your band is " + bandName + "! Sounds pretty cool to me.")