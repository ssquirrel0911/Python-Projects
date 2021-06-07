#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 20 Chapter 10 Lab Programming Exercise 5; Retail Item

#RetailItem function


import time

from SamanthaSquirrelAssignment20RetailClass import RetailItem 

def main():

    #Creates a list for retail item
    retailItem = makeList()

    #Displays data in a list
    print("This is the data that is entered: ")
    displayList(retailItem)


#makeList function ets data from the user for 3 retail items
#Function will return a a list of retail objects containing the data

def makeList():

    #Creates empty
    retailItemChart = []

    #Adds 3 RetailItem objects to the list
    #User will input a data for all 3 retail items
    print("Enter data for 3 retail products.")
    for count in range(1, 4):
        #Get retail item data
        print("Item " + str(count) + ":")
        retailItemItem = input("Enter retail product: ")
        retailItemUnits = int(input("Enter the number of units brought: "))
        retailItemPrice = float(input("Enter the item's price: "))
        print()

        #Creates a new RetailItem object in memory
        #and assigns it to retailItem variable

        retailItem = RetailItem(retailItemItem, retailItemUnits, retailItemPrice)

        #Adds objects to the list
        retailItemChart.append(retailItem)

        #Returns list
        return retailItemChart

#The displayList function accepts a list containing the objects as an argument
#and displays store data

def displayList(retailItemChart):
    for item in retailItemChart:
        print(item.getItem())
        print(item.getUnits())
        print(item.getPrice())
        print()

main()
        
time.sleep(3)
