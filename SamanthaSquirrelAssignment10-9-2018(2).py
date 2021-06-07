#Samantha Squirrel
#samantha.squirrel001@albright.edu
#Assignment 11 due 10-9-2018


#Chapter 5 programming exercise 15; Test Average and Grade

import time


def main():
    scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive = askForTestScores()
    average = calcAverage(scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive)
    printResults(average, scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive)

def askForTestScores():
    #User will input 5 random test scores test scores of choice
    scoreOne = float(input("Enter your first score:", ))
    scoreTwo = float(input("Enter your second score:", ))
    scoreThree = float(input("Enter your third score:", ))
    scoreFour = float(input("Enter your fourth score:", ))
    scoreFive = float(input("Enter your fifth score:", ))

    return scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive


def calcAverage(scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive):
    #Calculates the average of all test scores
    average = (scoreOne + scoreTwo + scoreThree + scoreFour + scoreFive) / 5
    return average
    
def determineGrade(score):
    #Determins what score the grade will recieve based on what the user input
    if( score < 60):
        return "F"
    elif( score < 70):
        return "D"
    elif( score < 80):
        return "C"
    elif( score < 90):
        return "B"
    if( score < 100):
        return "A"

def printResults(average, scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive):
    #Displays average score and seperate along with letter grade

    print("The average score for all tests combined is: ",
          format(average, ',.2f'),
          sep='')
    
    print("Score \t Letter Grade")
    print("---------------------")
    print(str(scoreOne) + "\t" + determineGrade(scoreOne), \
          str(scoreTwo) + "\t" + determineGrade(scoreTwo), \
          str(scoreThree) + "\t" + determineGrade(scoreThree), \
          str(scoreFour) + "\t" + determineGrade(scoreFour), \
          str(scoreFive) + "\t" + determineGrade(scoreFive), sep = "\n")

    
    

main()


time.sleep(3)
