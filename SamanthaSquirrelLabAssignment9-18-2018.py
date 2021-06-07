#Samantha Squirrel
#samantha.squirrel001@albright.edu

import time

#Lab assignments Programming Exercises

#Execise 1

dayOfWeek = int(input("Input a number in the range of 1 through 7:", )) #User should put in a number in the range of 1 through 7

if dayOfWeek == 1:
    print("Monday")
elif dayOfWeek == 2:
    print("Tuesday")
elif dayOfWeek == 3:
    print("Wednesday")
elif dayOfWeek == 4:
    print("Thursday")
elif dayOfWeek == 5:
    print("Friday")
elif dayOfWeek == 6:
    print("Saturday")
elif dayOfWeek == 7:
    print("Sunday")
else:
    print("The number you input cannot be recogonized " \
          "because there are only 7 days in a week.")

#Exercise 2

lengthOfRectangle1 = float(input("What is the length of your first rectangle?", )) #User will put in the first rectangle length
widthOfRectangle1 = float(input("What is the width of your first rectangle?", )) #User will put in the first rectangle width

lengthOfRectangle2 = float(input("What is the length of your second rectangle?", )) #User will put in the second rectangle length
widthOfRectangle2 = float(input("What is the width of your second rectangle?", )) #User will put in the second rectangle width 

areaOfRectangle1 = lengthOfRectangle1 * widthOfRectangle1
print("The area of your first rectangle is: ", areaOfRectangle1)

areaOfRectangle2 = lengthOfRectangle2 * widthOfRectangle2
print("The area of your second rectangle is:", areaOfRectangle2)

if areaOfRectangle1 > areaOfRectangle2:
    print("The area of your first rectangle is greater than your second rectangle.")#Will let user know the first rectangle area is bigger than the second
elif areaOfRectangle2 > areaOfRectangle1:
    print("The area of your second rectangle is greater than your second rectangle.") #Will let user know the second rectangle area is bigger than the first
elif areaOfRectangle1 == areaOfRectangle2:
    print("The area of both your rectangles are the same.")
else:
    print("You did a succesful job with inputting your values.") #Positive feedback for the user

#Exercise 3

ageOfUser = int(input("What is your age?", )) #User will input their age 

if ageOfUser <= 1:
    print("You are an infant.") #Will let user know if they are an infant
elif ageOfUser >= 1 or 1 <= 13:
    print("You are a child.") #Will let user know if they are a child
elif ageOfUser >= 13 or 13 <= 20:
    print("You are a teenager.")#Will let user know if they are an teenager
elif ageOfUser >= 20:
    print("You are an adult.")#Will let user know if they are an adult
else ageOfUser <= 0:
    print("You can't be any age less than 0.") #Will let user know they're not born yet

time.sleep(3)
