#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 20 Chapter 10 Programming Exercise 8; Cash Register
#CashRegister Function

import time

from SamanthaSquirrelAssignment20RetailClass import RetailItem
from SamanthaSquirrelAssignment20CashRegisterClass import CashRegister

def main():
    nameItem = inputItem()
    inputMoreItems(nameItem)
    display()


def inputItem():
    #User will input item they want to purchase
    nameItem = input("Enter the description of the item you will purchase: ")
    return nameItem

def inputMoreItems(nameItem):
    #User will input 'q' if they want to quit the program
    while name != 'q' or "Q":
        #User will input how much they are going to purchase
        quantity = int(input("Enter the quantity you are going to buy: "))
        pricePerUnit = float(input("Enter the price for 1 of the items: "))
        price =  quantity * pricePerUnit

        #Creates object from retail item class
        item = retail.RetailItem(item, units, price)
        cart.purchaseItem(item)

        nameItem = input("Enter the description of the item you will" \
                         "purchase or 'q' to quit program: ")


def display():
    #Displays the total of items to purchase
    print("Your total is: $", cart.getTotal(), sep = "") 

        
main()        
                   
time.sleep(3)
