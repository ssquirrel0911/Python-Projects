#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Chapter 4 Lab Assignment Programming Exercises and Lab problem

import time

#Program Exercise 2

totalBugs = 0

for count in range(5):
    counter = int(input("Please enter the amount of bugs you " \
                        "accumlated through day 1-5: "))#User will input how many bugs they found
    totalBugs += counter
print("This is the total number of bugs " \
      "you found after 5 days is: ", totalBugs)#Displays how much bugs the user found after five days

#Program Exercise 3

startTime = 0 #Starting time on treadmill
endTime = 31 #Ending time of treadmill
addedTime = 5 #Time increment for how long treadmill should go
addedCalories = 4.2 #Converts calories

#Prints a table
print('Time\tCalories Burned')
print('---------------------')

for time in range(startTime, endTime, addedTime):
    caloriesBurned = time * addedCalories
    print(time, '\t', format(caloriesBurned, '.1f'))

#Lab Program

word = input("Please input a word to decode for ASCII: ") #User will input a random word of choice

for letters in word:
    print("Current letter of word: ", letters)#Program will print out word user input
    print("The ASCII value of", ord(letters))#Program will show the numeric value of the input word
    print("The upper case value of", letters.upper())#Program wll show upper case value of the input word

time.sleep(3)
