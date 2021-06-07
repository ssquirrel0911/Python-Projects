#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 22 Chapter 12 Programming Exercise 4: Largest List Item

import time

def main():
    #Displays the max in the list 
    print(maxOfList([4, 3, 5, 192.6, 14, -2]))
    
def maxOfList(xs):
    if len(xs) == 1:
        #returns list to 0 if there isn't a number higher than 0
        return xs[0]
    elif xs[0] > xs [1]:
        xs.pop(1)
        return maxOfList(xs)
    else:
        xs.pop(0)
        return maxOfList(xs)

main()

time.sleep(3)
