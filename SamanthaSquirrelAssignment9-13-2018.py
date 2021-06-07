#Samantha Squirrel
#samantha.squirrel001@albright.edu
#9-13-2018 Assignment 

#Short IF ELSE program 1

import time

votingAge = 18
retiredAge = 67

age = int(input("How old are you?", ))
print ("My age is", age)

if age > votingAge:
    print("You are old enough to vote.")
    
if age < retiredAge:
    print("Your age before you can retire is", retiredAge - age)

else:
    if age < votingAge:
        print("You're not able to vote yet.")

#Short IF ELSE program 2

x = 1
y = 0
z = -1

print(bool(x)) #Print out True
print(bool(y)) #Print out False
print(bool(z)) #Print out True

#Chapter 3 Algorithm workbench

#Algorithm 1

if x > 100:
    y = 20
    z = 40

#Algorithm 2

if a < 10:
    b = 0
    c = 1

#Algorithm 3

if a < 10:
    b = 0
else:
    b = 99
#Algorithm 4
if score >= A_SCORE:
    print('Your grade is A.')
elif score >= B_SCORE:
    print('Your grade is B.')
elif score >= C_SCORE:
    print('Your grade is C.')
elif score >= D_SCORE:
    print('Your grade is D.')
else:
    print('Your grade is F.')


time.sleep(3)
