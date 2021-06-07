#Samantha Squirrel
#samantha.squirrel001@albright.edu
#Assingment 19 Chapter 10 Algorithm Workbench: 2

import time

#Book class simulates the attributes for a book
class Book(object):

    #Initializes the attributes
    def __init__(self, bookTitle, authorName, publisher):
        self.__bookTitle = bookTitle
        self.__authorName = authorName
        self.__publisher = publisher

    #Method accepts argument for book title
    def setBookTitle(self, bookTitle):
        self.__bookTitle = bookTitle

    #Method accepts argument for author's name
    def setAuthorTitle(self, authorName):
        self.__authorName = authorName

    #Methods accepts argument for publish name
    def setPublisherName(self, publisher):
        self.__publisher = publisher

    #Setting get_method returns the book title

    def getBookTitle(self):
        return self.__bookTitle

    #Setting get_method returns the author's name
    def getAuthorName(self):
        return self.__authorName

    #Setting get_method returns the publisher's name
    def getPublisherName(self):
        return self.__publisher

    #Storing method for the class
    def __str__(self):
        return "The book title is %s, the author's name is %s, the publisher name is %s" %(self.__bookTitle, self.__authorName, self.__publisher) 


time.sleep(3)
