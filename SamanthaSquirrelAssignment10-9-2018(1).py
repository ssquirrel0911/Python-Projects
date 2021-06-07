#Samantha Squirrel
#samantha.squirrel001@albright.edu
#Assignment 11 due 10-9-2012


#Chapter 5 Programming Exercise 8; Paint Job estimator

import time

def main():
    wallSpaceRequired = askForWallSpace()
    priceOfPaint = askForPriceOfPaint()
    paintRequired = totalPaintRequired(wallSpaceRequired)
    laborRequired = hoursOfLabor(wallSpaceRequired)
    costOfPaint = totalCostOfPaint(priceOfPaint, paintRequired)
    laborCharges = totalLaborCharge(laborRequired)
    totalCost = paintJobTotal(laborCharges, costOfPaint)
    totalBill(wallSpaceRequired, priceOfPaint, paintRequired, laborRequired, costOfPaint, laborCharges,
              totalCost)
    


def askForWallSpace():
    wallSpaceRequired = float(input("What is the wall space required for this paint job?", ))
    return wallSpaceRequired

def askForPriceOfPaint():
    priceOfPaint = float(input("What is the price of the paint you obtained?", ))
    return priceOfPaint

def totalPaintRequired(wallSpaceRequired):
    paintRequired = (wallSpaceRequired/ 112) * 1
    return paintRequired    

def hoursOfLabor(wallSpaceRequired):
    laborRequired = (wallSpaceRequired / 112) * 8
    return laborRequired

def totalCostOfPaint(priceOfPaint, paintRequired):
    costOfPaint = paintRequired * priceOfPaint
    return costOfPaint

def totalLaborCharge(laborRequired):
    chargePerHour = 35.00
    laborCharges = laborRequired * chargePerHour
    return laborCharges

def paintJobTotal(laborCharges, costOfPaint):
    totalCost = laborCharges + costOfPaint
    return totalCost

def totalBill(wallSpaceRequired, priceOfPaint, paintRequired, laborRequired, costOfPaint, laborCharges,
              totalCost):
    print("The wall space required for the paint job is:", wallSpaceRequired)
    print("The paint required for the paint job is:", paintRequired)
    print("The cost of the price of paint is:$", priceOfPaint)
    print("The hours of labor that will happen is:", laborRequired)
    print("The cost of paint required for paint job is: $",
          format(costOfPaint, ',.2f'),
          sep='')
    print("The total cost of the whole project is: $",
          format(totalCost, ',.2f'),
          sep='')
    print("The total charge of labor is: $",
          format(laborCharges, ',.2f'),
          sep='')
    print("The total charge of the full paint job is: $",
          format(totalCost, ',.2f'),
          sep='')
    


main()


time.sleep(3)
