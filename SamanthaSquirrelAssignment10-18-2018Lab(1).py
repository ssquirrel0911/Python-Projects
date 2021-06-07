#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Chapter 6 Lab assignment Programming Exercise 4; Item Counter

import time



def main():

    readFileWithExecption()



def readFileWithExecption():
    try:
        namesFile = open("names.txt.", "r")
        line = namesFile.readline()
        numberOfLines = 0

        while line != "":
            numberOfLines = numberOfLines + 1
            line = namesFile.readline()
            print( "The file has ", numberOfLines, "lines" )

        namesFile.close()

    except IOError:
        print("An error occured while trying to read the file.")




time.sleep(3)



main()
