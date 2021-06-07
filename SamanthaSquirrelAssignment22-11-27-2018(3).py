#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 22 Chapter 12 Programming Exercise 5; Recursive List Sum

import time

def main():
    print(sumOfList([4, 4, 3, 5, 192.6, 14, -2]))

def sumOfList(xs):
    if len(xs) == 1:
        #returns list as 0 is xs is not qual to 1
        return xs[0]
    else:
        return xs[0] + sumOfList(xs[1:])
    
main()

time.sleep(3)
