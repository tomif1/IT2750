#########################################
#### IT 2750 - Lab 05                   #
#### Regular Expressions                #
#### Author: Oluwatomisin Fayomi        #
#########################################

# Import the regular expressions module
import re

# Function that takes a file and loads it into
# a Python list variable and returns that variable
def loadLogIntoList(filename):
   with open(filename) as f:
      lines = f.read().splitlines()
   return lines

# Ask the user to input a file name
filename = input("Type in the filename for the log to analyze: ")

# Load each line of the file into a list of strings
lines = loadLogIntoList(filename)

# Create a placeholder variable (a list of strings) to
# hold the IP addresses and users we find in the log file
ipAddresses = []
users = []

# Loop through each line of the file
for line in lines:
   
   #############################################################
   ####  Part 1: Create a new python regular expression object 
   ####          by compiling an expression to look for an
   ####          IP address
   #############################################################
   ipRegEx = re.compile(r'[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?')
   #print(ipRegEx)
   
   # Search the contents of each line for a match. If there is a
   # match and that match doesn't already exist in the list, append
   # it to the list
   ipSearchResult = ipRegEx.search(line)
   if ipSearchResult != None and ipSearchResult.group() not in ipAddresses:
      ipAddresses.append(ipSearchResult.group())
      
   #############################################################
   ####  Part 2: Create a new python regular expression object 
   ####          by compiling an expression to look for a user 
   ####          account(as a DOMAIN\username combination)
   #############################################################
   userRegEx = re.compile(r'\w([^\s]+)\\\w([^\s]+)')
   
   # Search the contents of each line for a match. If there is a
   # match and that match doesn't already exist in the list, append
   # it to the list
   userSearchResult = userRegEx.search(line)
   if userSearchResult != None and userSearchResult.group() not in users:
      users.append(userSearchResult.group())

#############################################################
####  Part 3: Loop through each IP address and display
####          each IP address found to the user
#############################################################

# WRITE CODE HERE
for x in ipAddresses:
   print("Found IP Address:  ",x)
print()
   
#############################################################
####  Part 4: Loop through each username (shown as a
####          DOMAIN\username combination) to the user
#############################################################

# WRITE CODE HERE
for x in users:
   print("Found User Account:  ",x)
print()