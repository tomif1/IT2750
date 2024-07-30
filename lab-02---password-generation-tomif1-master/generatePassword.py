#######################################
# IT 2750 - Lab 02                    #
# Generate a secure password          #
# Author: Oluwatomisin Fayomi         #
# S#: Your S01248177                  #
#######################################

# Import libraries needed for this lab
import random
import string


# Define a method generatePassword that:
# - Has the following parameters:
#   + length -> int, length of password to be created
#   + upper -> bool, True means include uppercase letters, False means
#              do not include uppercase letters
#   + lower -> bool, True means include lowercase letters, False means
#              do not include lowercase letters
#   + numbers -> bool, True means include numbers, False means
#                do not include numbers
#   + symbols -> bool, True means include symbols, False means
#                do not include symbols
# [You will have to define parameters in the function below - Remove this comment line placeholder!]
def generatePassword(length, upper, lower, number, symbol):
    # Create local variables for the set of characters that can be used
    # and the new password that will be returned from the function
    chars = ""
    newPassword = ""

    if upper == True:
        chars += string.ascii_uppercase
    if lower == True:
        chars += string.ascii_lowercase
    if number == True:
        chars += string.digits
    if symbol == True:
        chars += string.punctuation


    # Use if statements and the string.ascii_ constants to add the various
    # character sets to the local variable tracking what characters to be
    # used (https://docs.python.org/3/library/string.html, see "String 
    # constants" for reference)
    # [Write code here - Remove this comment line placeholder!]
    while length > 0:
        newPassword += random.choice(chars)
        length -= 1
    # Create a loop (of any type) to add a random character from the set of
    # characters (hint: using random.choice(...)) to the new password
    # placeholder variable
    # [Write code here - Remove this comment line placeholder!]

    # Return the new password as the function's return value
    return newPassword

# Print a welcome message
print('====================================================')
print('==== WELCOME TO THE ULTIMATE PASSWORD GENERATOR ====')
print('====================================================')

# Ask the user how long of a password they want
# [Write code here - Remove this comment line placeholder!]

# Ask the user if they want to use uppercase, lowercase, numbers
# and symbols in separate input statements. Remember to properly
# handle variable types! (hint: bool(...) converts to bool, 
# int(...) converts to int, str(...) converts to string)
# [Write code here - Remove this comment line placeholder!]
length = int(input("How long should the password be? "))
upper = input("Use UPPERcase letters? 1 = Yes, 0 = No: ")
if upper == "1":
    upper = True
else:
    upper = False
lower = input("Use lowercase letters? 1 = Yes, 0 = No: ")
if lower == "1":
    lower = True
else:
    lower = False
numbers = input("Use numbers? 1 = Yes, 0 = No: ")
if numbers == "1":
    numbers = True
else:
    numbers = False
symbols = input("Use symbols? 1 = Yes, 0 = No: ")
if symbols == "1":
    symbols = True
else:
    symbols = False
print  (length,upper,lower,numbers,symbols)
# Call the generatePassword function and pass in the user's choices
# and display the return value to the user
print('----------------------------------------------------')
print('Generating password...')
print('----------------------------------------------------')
# [You will have to pass arguments into the generatePassword function below - Remove this comment line placeholder!]
print("Your new password is: " + generatePassword(length, upper, lower, numbers, symbols))
print('====================================================')
