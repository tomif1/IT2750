#############################################################################
#### IT 2750 - Lab 06                                                       #
#### File Forensics                                                         #
#### Author: Oluwatomisin Fayomi                                            # 
#### !!! IF YOU DO NOT PUT YOUR NAME HERE YOU WILL RECEIVE A ZERO SCORE !!! #
#############################################################################

# Import required modules
from importlib.resources import read_text
from pathlib import Path
import os
from turtle import end_fill

###############################################################
# Part 1: Ask the user for the ABSOLUTE path to Bruce Wayne's 
#         folder and save it to a string variable
###############################################################

myPath = str(input("What is the path to the Bruce Wayne folder\n"))

###############################################################
# Part 2: Convert that string to a Path variable
###############################################################

path = Path(myPath)
print(path)

###############################################################
# Part 3: List all files in the folder and display the name of
#         each file to the user
###############################################################
files = os.listdir(path)
for x in files:
    print("Found one of Bruce's files...",x)


###############################################################
# Part 4: Open up each file and look for the string "Batman".
#         If Batman is found, let the user know that 
#         we have found Batman and what file we found the
#         string in
#
#         HINT: Here is an example of looking for a substring
#               within a string varible (we'll call the variable
#               fileContents) (from previous lessons)
#
#         if "Batman" in fileContents:
#            print("Found Batman!!")
###############################################################
print()
for filecontents in files:
    fileLocation = myPath+'\\'+filecontents
    myFile = open(fileLocation)
    myFullFileContents = myFile.read()
    if "Batman" in myFullFileContents:
        print("Ha! We found Batman! He admitted it in", filecontents)
        break
    #else:
     #   print("Batman not in", filecontents)
