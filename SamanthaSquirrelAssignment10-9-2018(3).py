#Samantha Squirrel
#samantha.squirrel001@albright.edu
#Assignment 11 due 10-9-2018

import time

#Chapter 5 programming exercise 11; Math Quiz

import random

randomNumberOne = random.randint(1, 250)
randomNumberTwo = random.randint(1, 250)

def main():
    answer = askUserQuestion()
    checkUserAnswer(answer)


def askUserQuestion():
    global randomNumberOne
    global randomNumberTwo
    #User will input the correct answer
    answer = int(input("What is " + str(randomNumberOne) + " + " + \
              str(randomNumberTwo) + " ?: "))
    return answer

def checkUserAnswer(answer):
    global randomNumberOne
    global randomNumberTwo
    #Displays if answer if answer is correct or not correct
    correctAnswer = randomNumberOne + randomNumberTwo
    if answer == correctAnswer:
        print("Correct!")
    else:
        print("That is the wrong answer. The correct answer is", correctAnswer)

    
main()







time.sleep(3)
