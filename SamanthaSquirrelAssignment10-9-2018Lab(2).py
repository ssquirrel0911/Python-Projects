#Samantha Squirrel
#samantha.squirrel001@albright.edu
#Assignment 11 due 10-9-2018


#Chapter 5 programming exercise 4; Automobile Costs


import time

def main():
    loanBill = askUserForMonthlyLoanBill()
    insuranceBill = askUserForMonthlyInsurance()
    gasBill = askUserForMonthlyGasBill()
    maintenanceBill = askUserForMaintenanceBill()
    annualCost = annualExpense(loanBill, insuranceBill, gasBill, maintenanceBill)
    exspenseStatement(loanBill, insuranceBill, gasBill, maintenanceBill)

    


def askUserForMonthlyLoanBill():
    #User will input their monthly loan payment
    loanBill = float(input("What is your monthly loan payment?", ))
    return loanBill

def askUserForMonthlyInsurance():
    #User will input their monthly insurance bill
    insuranceBill = float(input("What is your monthly"\
                                "insurance bill?", ))
    return insuranceBill

def askUserForMonthlyGasBill():
    #User will input their monthly gas bill
    gasBill = float(input("What is your monthly gas bill?", ))
    return gasBill

def askUserForTireBill():
    #User will input their monthly tire bill
    tireBill = float(input("What is your monthly tire bill?", ))
    return tireBill

def askUserForMaintenanceBill():
    #User will input their monthly maintenance bill
    maintenanceBill = float(input("What is your monthly maintenance bill?", ))
    return maintenanceBill 

def annualExpense(loanBill, insuranceBill, gasBill, maintenanceBill):
    #Calculates all bills multiplied by 12 and then added together to make annual bill
    annualCost = (loanBill * 12) + (insuranceBill * 12) + (gasBill * 12) + (maintenanceBill * 12)
    return annualCost

def expenseStatement(loanBill, insuranceBill, gasBill, maintenanceBill):
    #Displays all monthly bills and annual bill
    print("Your monthly bill for your loan is $", loanBill)
    print("Your monthly bill for your insurance is $", insuranceBill)
    print("Your monthly bill for your gas is $", gasBill)
    print("Your monthly bill for your maintenance is $", maintenanceBill)
    print("Your total annual expense of all your automobile is $",
          format(annualCost, ',.2f'),
          sep='')
    
main()



time.sleep(3)

