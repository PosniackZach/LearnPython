import random


strngName = input("Welcome to the Dice Game! What's your name? ")

print("Hi " + strngName + "! We just have a few questions for you to get started.")

numDice = input("How many dice will you be playing with today? ")

numSides = input("How many sides would you like your die to have? ")

numDice = int(numDice)

numSides = int(numSides)

lstRoll = []


for i in range(numDice):

    x = random.randint(1, numSides)

    lstRoll.append(x)

print("The Results are in! You rolled:") print(*lstRoll, sep=",")




