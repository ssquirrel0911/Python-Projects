#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 22 Chapter 12 Programming Exercise 3: Recursive Lines

import time

def main():
    asterisks(4)

def asterisks(n):
    #Make n is a positive integer
    if n > 1:
        asterisks(n - 1)
        print("*'" * n)
    else:
        print("*")


main()

time.sleep(3)
