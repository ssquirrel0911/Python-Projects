#Samantha Squirrel
#samantha.squirrel001@albright.edy

#Assignment 20 Chapter 10 Lab Programming Exercise 5; Retail Item

import time

class RetailItem:

    #The __init__ method initializes the attributes

    def __init__(self, item, units, price):
        self.__item = item
        self.__units = units
        self.__prices = price


    #set_item methods accepts argument for user's name

    def setItem(self, item):
        self.__item = item

    #set_units methods accepts argument for user's IDNumber

    def setUnits(self, units):
        self.__units = units

    #set_price methods accepts argument for user's department

    def setPrice(self, price):
        self.__prices = price

    #get_item methods method returns name

    def getItem(self):
        return self.__item

    #get_units methods method returns ID Number

    def getUnits(self):
        return self.__units

    #get_price methods returns department

    def getPrice(self):
        return self.__prices

time.sleep(3)   
