#Samantha Squirrel
#samantha.squirrel001@albright.edy

#Assignment 20 Programming Exercise 8; Cash Register

import time

class CashRegister:
    #Initializes a CashRegister object with an empty list for cart
    #This is where RetailItems to be purchased will be stored
    def __init__(self):
        self.__cart = []

    #Adds purchased item to cart
    def purchaseItem(self, item):
        #Creates list of description of items in cart
        cartDescriptions = []
        for i in range(len(self.__cart)):
            self.__cart[i].setUnits(self.__cart[i].getUnits() \
                                    + item.getUnits())
            self.__cart[i].setPrice(self.__cart[i].getPrice() \
                                    + item.getPrice())

    #Caculates and returns total cost of all items in cart
    def getTotal(self):
        total = 0
        for item in self.__cart:
            total += item.getPrice()
        return format(total, ',.2f')

    #Displays a list of all items in the cart
    def showCart(self):
        print("Yout cart")
        for item in self.__cart:
            print(item)
            print("------------")

    #Clears content of the cart if needed
    def clear(self):
        self.cart = []
        
time.sleep(3)
