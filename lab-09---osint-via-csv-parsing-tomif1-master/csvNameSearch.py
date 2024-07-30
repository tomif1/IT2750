##########################################
#### IT 2750 - Week 10 Lab               #
#### More OSINT With CSV Files           #
#### Author: Oluwatomisin Fayomi         #
##########################################

import csv

# Print a nice title for the user
print("People Finder v0.1")
print("==================")

# Let the user know that we are loading the data
print("Loading data...")

contactsFile = open('fake_data.csv')
contactsReader = csv.reader(contactsFile)
contactsDictionary = dict()

# Part 1: Save each row into the dictionary contactsDictionary
# with each key being the email address contained in that row
# and the value being the row itself+--

# WRITE YOUR CODE HERE
for row in contactsReader:
    contactsDictionary[row[1]] = row
# Let the user know that the data loading is complete
print("Data set loaded!")

# Part 2: Define a function that returns a full name given an
# email address passed into parameter email. This function will
# look the value up in the dictionary contactsDictionary. If a key
# does not exist, return an empty string
def findName(email):


    # WRITE YOUR CODE HERE
    if email in contactsDictionary:
        return contactsDictionary[email][0]
    else:
        return ""
# Part 3: Define a function that returns a country given an
# email address passed into parameter email. This function will
# look the value up in the dictionary contactsDictionary. If a key
# does not exist, return an empty string
def findCountry(email):
    
    # WRITE YOUR CODE HERE
    return contactsDictionary[email][2]

# Part 4: Ask the user to enter an email address to search. Call the
# findName function to return the first and last name corresponding to
# the email address to the user. If the result is an emptry string, let the
# user know nothing was found, otherwise display the name and the email (you
# will also need to call findCountry)

inputString = ""

# Loop while the user has not entered STOP
while inputString != "STOP":
    print("What email would you like to search? (Type STOP to exit)")
    inputString = input(">> ")
    if inputString != "STOP":

        # WRITE YOUR CODE HERE:
        #    Call the findName function to return the first and last name 
        #    corresponding to the email address to the user. If the result
        #    is an emptry string, let the user know nothing was found, 
        #    oherwise display the name and the email (you will also need to
        #    call findCountry)
        if findName(inputString) != "":
            print("Match found! {0} lives in {1}.".format(findName(inputString),findCountry(inputString)))
        else: print("No email found.")
    # If the user typed STOP, go to the start of the while loop. The
    # loop will exit automatically and end the script
    else:
        continue
