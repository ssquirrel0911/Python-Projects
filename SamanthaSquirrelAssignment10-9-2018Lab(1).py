#Samantha Squirrel
#samantha.squirrel001@albright.edu
#Assignment 11 due 10-9-2018


#Chapter 5 programming exercise 3; How much insurance?

import time

def main():
    replacementCost = askForReplacementCost()
    minimumInsurance = bestMinimumInsurance(replacementCost)
    insuranceDetails(replacementCost, minimumInsurance)

def askForReplacementCost():
    #User will input their replacement costs
    replacementCost = float(input("What is the replacement cost of your establishment?", ))
    return replacementCost

def bestMinimumInsurance(replacementCost):
    #Calculates replacement cost to find user's minimum insurance
    minimumInsurance = (80/100) * replacementCost
    return minimumInsurance

def insuranceDetails(replacementCost, minimumInsurance):
    #Displays the replacement costs and minimum insurance 
    print("The replacement cost of your estbalishment replacement is $", replacementCost)
    print("The minimum insurance required for your establishment is $",
          format(minimumInsurance, ',.2f'),
          sep='')




main()


time.sleep(3)
