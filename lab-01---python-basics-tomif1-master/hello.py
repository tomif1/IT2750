######################################
# IT 2750 - Lab 01                   #
# Hello from python!                 #
# Author: Oluwatomisin Fatomi        #
# ID Number: s01248177               #
######################################

####################################################
# Part 1: Creating variables and using expressions #
####################################################

# Create two variables. Make one equal to 67 and one to 13.
spam = 67
spam2 = 13

# Add the two variables and display it to the user
spam3 = spam + spam2
print(spam3)

# Subtract the two variables and display it to the user
spam3 = spam - spam2
print(spam3)
# Multiply the two variables and display it to the user
spam3 = spam * spam2
print(spam3)

# Divide the two variables and display it to the user
spam3 = spam / spam2
print(spam3)

######################################################
# Part 2: Accepting user input and using expressions #
######################################################

# Replace each variable with user input. Ask the user
# to enter a number for each variable
spam = int(input("Please enter a number for variable 1:"))
spam2 = int(input("Please enter a number for variable 2:"))

# Add the two variables and display it to the user
spam3 = spam + spam2
print("Adding variables:", spam3)

# Subtract the two variables and display it to the user
spam3 = spam - spam2
print("Subtracting variables:", spam3)

# Multiply the two variables and display it to the user
spam3 = spam * spam2
print("Multiplying variables:", spam3)

# Divide the two variables and display it to the user
spam3 = spam / spam2
print("Dividing variables:", spam3)

###################################################################
# Part 3: Accepting user input and using expressions with strings #
###################################################################

# Replace each variable with user input. Ask the user
# to enter a string for each variable
spam = input("Please enter a STRING for variable 1:")
spam2 = input("Please enter a STRING for variable 1:")

# Join the two strings together and display them to the user
print(spam + spam2)

# Repeat the first string three times and display to the user
print(spam * 3)

# Repeat the second string three times and display to the user
print(spam2 * 3)


############################################################
# Congrats! Now, test the assignment and submit to GitHub! #
############################################################
