#Samantha Squirrel
#CSC 141 Chapter 5 Lab
#Assignment 10 due 10-4-2018

#Programming Exercise 2

def main():
    purchaseAmount = askUserForPurchaseAmount()
    stateTax = stateTaxTotal(purchaseAmount)
    countyTax = countyTaxTotal(purchaseAmount)
    totalTax = fullTotalTax(stateTax, countyTax) 
    totalSale = purchaseTotal(purchaseAmount, totalTax)
    print("Your total with state tax is", stateTax)
    print("Your total with county tax is", countyTax)
    print("Your total purchase including taxes is",
          format(totalSale, ',.2f'),
          sep='')

def askUserForPurchaseAmount():
    #Enter your full purchase
    purchaseAmount = float(input("What is you full purchase amount?", ))
    return purchaseAmount

def stateTaxTotal(purchaseAmount):
    stateTax = 0.05 * purchaseAmount
    return stateTax

def countyTaxTotal(purchaseAmount):
    countyTax = 0.025 * purchaseAmount
    return countyTax

def fullTotalTax( stateTax, countyTax):
    totalTax = stateTax + countyTax
    return totalTax

def purchaseTotal(purchaseAmount, totalTax):
    totalSale = purchaseAmount + totalTax
    return totalSale
    

main()


time.sleep(3)
