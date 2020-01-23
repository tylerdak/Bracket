from tkinter import *
from tkinter.filedialog import askopenfilename
import csv
from isInt import isInt
from random import *


Tk().withdraw()

print("Welcome to Bracket Helper!")
print("The easiest way to make and decide through a bracket!\n")

validFile = False
print("Let's start with getting your .csv file with the list of items.")

while (not validFile):
    #opens dialog box which will return a filename
    csvFilename = askopenfilename()

    if (csvFilename == ''):
        validFile = False
        print("Please choose your .csv file so we can make your bracket.")
        print("[Press ENTER or RETURN]")
        wait1 = input()
    elif (not csvFilename.endswith(".csv")):
        validFile = False
        print("Please choose a valid .csv file so we can make your bracket.")
        print("[Press ENTER or RETURN]")
        wait1 = input()

    else:
        validFile = True


file = open(csvFilename)
exampleReader = csv.reader(file)
itemList = []

#return certain number of winners
print("How many winners would you like in the end?",end=" ")
winnerNum = input()

while not isInt(winnerNum):
    print("Please enter a valid integer.")
    print("How many winners would you like in the end?",end=" ")
    winnerNum = input()

#add each item in the .csv to one list
for item in exampleReader:
    itemList.append(item[0])

rounds = 0

acceptableChoices = [1,2,";","'"]

#this while loop should contain the steps that happen in each "round"
while (not len(itemList) == int(winnerNum)):
    print()
    rounds += 1
    print("ROUND " + str(rounds))
    print(str(len(itemList)) + " items remaining!")
    shuffle(itemList)
    toRemove = []
    numOfContenders = len(itemList)
    faceoffNum = int(numOfContenders / 2)

    for i in range(1, faceoffNum+1):
        con1 = itemList[(i * 2) - 2]
        con2 = itemList[(i * 2) - 1]
        cons = [con1, con2]

        choice = 0

        while (not (choice in acceptableChoices)):
            print("Choose the best of these options: ")
            print("1: " + con1)
            print("2: " + con2)

            print("Choice: ",end="")
            choice = input()
            if isInt(choice):
                choice = int(choice)
            elif (choice == ";"):
                choice = 1
            elif (choice == "'"):
                choice = 2


        print("You chose " + cons[choice-1] + ".\n\n")
        cons.remove(cons[choice-1])
        if ((len(itemList) - len(toRemove) - 1) >= int(winnerNum)):
            toRemove.append(cons[0])

    for item in toRemove:
        itemList.remove(item)



print("The winners have been chosen!")
for winner in itemList:
    print(winner)
