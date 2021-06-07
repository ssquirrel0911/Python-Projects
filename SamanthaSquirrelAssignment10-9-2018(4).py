#Samantha Squirrel
#samantha.squirrel001@albright.edu
#Assignment 11 due 10-9-2018

import time

#Chapter 5 programming exercise 20; Random Number Guessing Game

import random



def main():

    congratulateUser = False
    beginGame = True

    while congratulateUser or beginGame:
        randomNumber = createRandomNumber()
        answer = askUserQuestion()
        message = checkUserAnswer(answer, randomNumber)

        while message != "Good Job!":
            print (message)
            answer = askUserQuestion("Try again: ")
            message = checkUserAnswer(answer, randomNumber)

        print(message)
        congratulateUser = True

def createRandomNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber

def askUserQuestion( message = "What is the random number?" ):
    #User will input the correct answer
    answer = int(input(message))
    return answer

def checkUserAnswer(answer, randomNumber):
    #Displays if answer if answer is correct or not correct
    if answer > randomNumber:
        return "Too high!"
    elif answer < randomNumber:
        return "Too low!"
    else:
        print("Good job!")

    
main()







time.sleep(3)

