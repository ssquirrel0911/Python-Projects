#Samantha Squirrel
#samantha.squirrel001@albright.edu

import time

#Assignment 9-18-2018 Exercises 4 - 8

#Exercise 4
romanNumeral = int(input("Input a number in the range of 1 through 10:", )) #User should put in a number in the range of 1 through 10

if romanNumeral == 1:
    print("I")
elif romanNumeral == 2:
    print("II")
elif romanNumeral == 3:
    print("III")
elif romanNumeral == 4:
    print("IV")
elif romanNumeral == 5:
    print("V")
elif romanNumeral == 6:
    print("VI")
elif romanNumeral == 7:
    print("VII")
elif romanNumeral == 8:
    print("VIII")
elif romanNumeral == 9:
    print("IX")
elif romanNumeral == 10:
    print("X")
else:
    print("The number you input cannot be recogonized " \
          "because you are only allowed to put a number through" \
          "the range of 1 through 10.") #Program will tell user they cannot input another number other than 1 through 10

#Exercise 5

mass = float(input("What is the mass of the object?", )) #User will input the mass of their object

weight = mass * 9.8

print("The weight of your object is:", weight)

if weight > 500:
    print("The object is too heavy.") #Program will tell user object is too heavy
elif weight < 100:
    print("The object is too light.") #Program will tell user object is too light
else:
    print("The object is an okay weight.") #Program will tell user object is a fine weight

#Exercise 6

month = int(input("Enter a month in numeric form: ", )) #User must put in a numerical month
day = int(input("Enter a day in numeric form: ", )) #user must put in a numerical day of month
year = int(input("Enter a two digit year: ", )) #User must put in a two digit year

if month * day == year:
    print("The date is magic.") #Program will tell user the date is magic
else:
    print("The date is not magic.") #Program will tell user date is not magic

#Exercise 7

primaryColorOne = input("Enter your first primary color: ", ) #User will put in a primary color of red, blue or yellow
primaryColorTwo = input("Enter your second primary color: ", )#User will put in a primary color of red, blue or yellow

if primaryColorOne == "red" and primaryColorTwo == "blue":
    print(primaryColorOne + " mixed with " + primaryColorTwo + " makes purple")#User will get purple for this input
elif primaryColorOne == "blue" and primaryColorTwo == "red":
    print(primaryColorOne + " mixed with " + primaryColorTwo + " makes purple")#User will get purple for this input
elif primaryColorOne == "red" and primaryColorTwo == "yellow":
    print(primaryColorOne + " mixed with " + primaryColorTwo + " makes orange")#User will get orange for this input
elif primaryColorOne == "yellow" and primaryColorTwo == "red":
    print(primaryColorOne + " mixed with " + primaryColorTwo + " makes orange")#User will get orange for this input
elif primaryColorOne == "blue" and primaryColorTwo == "yellow":
    print(primaryColorOne + " mixed with " + primaryColorTwo + " makes green")#User will get green for this input
elif primaryColorOne == "yellow" and primaryColorTwo == "blue":
    print(primaryColorOne + " mixed with " + primaryColorTwo + " makes green")#User will get green for this input
else:
    print("The colors you input are not primary colors.") #Tells user they cannot put anything other than primary colors

#Exercise 8

attenders = int(input("How many people are going to attend your cookout?", )) #User will put the number of people attending the cookout

hotdogsGiven = int(input("How many hotdogs will people recieve" \
                            "for attending your cookout?", ))
hotdogPackage = 10
hotdogBuns = 8

hotdogsNeeded = attenders * hotdogsGiven
minimumHotdogPackage = hotdogsNeeded * hotdogPackage
minimumHotdogBuns = hotdogsNeeded * hotdogBuns

leftoverHotdogPackage = hotdogsNeeded % hotdogPackage
leftoverHotdogBuns = hotdogsNeeded % hotdogBuns

noLeftoverHotdogPackages = ((hotdogsNeeded // hotdogPackage) * hotdogPackage + \
                                    hotdog_package) - hotDogsNeeded
noLeftoverHotdogBuns = ((hotdogsNeeded // hotdogBuns) * hotdogBuns + \
                                    hotdogBuns) - hotdogsNeeded
print()

if leftoverHotdogPackage > 0:
    print("The minimum hotdog packages required" \
          "for your cook out is: ", int(minimumHotdogPackage) + 1)
else:
    print("The minimum hotdog packages required" \
          "for your cook out is: ", int(minimumHotdogPackage))
if leftoverHotdogBuns > 0:
    print("The minimum hotdog buns required" \
          "for your cook out is: ", int(minimumHotdogBuns) + 1)
else:
    print("The minimum hotdog packages required" \
          "for your cook out is: ", int(minimumHotdogBuns))
if noLeftoverHotdogPackage > 0:
    print("The hotdogs that will be" \
          "left over after cook out: ", int(noLeftoverHotdogPackages))
else:
  print("The hotdogs that will be" \
        "left over after cook out: ", int(noLeftoverHotdogPackages))
if noLeftoverHotdogBuns > 0:
    print("The hotdogs buns that will be" \
          "left over after cook out: ", int(noLeftoverHotdogBuns))
else:
  print("The hotdogs buns that will be" \
        "left over after cook out: ", int(noLeftoverHotdogBuns))



time.sleep(3)
