######################################
# IT 2750 - Final Project            #
# Authors:                           #
# Michael Markwood - S01225355       #
# Oluwatomisin Fayomi - S01248177    #
# Michael Kupresanin - S00052721     # 
# Eric Oldag - S00635901             #
# Leinaliz Martinez- S01063127       #
######################################

# Import libraries needed for this lab
import random
import string
import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"
key      = "zjrekydnqoluaxmicvpgtfbhws"

# Set Background and text color
print("\033[1;32;40m")

#setup to ask the user for input to generate password
def passwordMenu():
    """Function to collect data from user to generate password"""
    # Print a welcome message
    print('===========================================================')
    print('  _______                     ____     _____               ') 
    print(' |__   __|                   |___ \   |_   _|              ')
    print('    | | ___  __ _ _ __ ___     __) |    | |  _ __   ___    ')
    print('    | |/ _ \/ _` | \'_ ` _ \   |__ <     | | | \'_ \ / __|   ')
    print('    | |  __/ (_| | | | | | |  ___) |   _| |_| | | | (__ _  ')
    print('    |_|\___|\__,_|_| |_| |_| |____( ) |_____|_| |_|\___(_) ')
    print('                                  |/                       ')
    print('===========================================================') 
    print('================  Password Generator 1.0  =================') 
    print('===========================================================') 

    #
    #
    # Ask the user how long of a password they want and return a message
    # if outside length requirements
    while True:
        try:
            length = int(input
            ("How many characters do you want your password to be ? "))
        except ValueError:
            #Set red text for error message
            print("\033[1;31;40m")
            print(''\
            '===========================================================')
            print(''\
                '| Please choose a password between 3 and 18 characters.   |') 
            print(''\
                '===========================================================') 
            continue
        if length < 3 or length > 18:
            #Set red text for error message
            print("\033[1;31;40m")
            print(''\
            '===========================================================') 
            print(''\
                '| Please choose a password between 3 and 18 characters.   |') 
            print(''\
            '===========================================================') 
            continue
        else:
            #Set green text for normal operation
            print("\033[1;32;40m")
            break
   
    # Ask the user if they want uppercase letters
    upper = int(input
    ("Do you want to include UPPERCASE Letters ? 1 = Yes , 0 = No "))
    # Ask the user if they want lowercase letters
    lower = int(input
    ("Do you want to include lowercase Letters ? 1 = Yes , 0 = No "))
    # Ask the user if they want numbers included
    numbers = int(input
    ("Do you want to include numbers ? 1 = Yes , 0 = No "))
    # Ask the user if they want to include symbols
    symbols = int(input
    ("Do you want to include symbols ? 1 = Yes , 0 = No "))

    #Check to make sure the user didn't select no for all options
    if upper == False and lower == False and numbers == False and \
        symbols == False:
        #Set red text for error message
        print("\033[1;31;40m")
        print('===========================================================') 
        print('| You must select at least one option!                    |') 
        print('===========================================================') 
        #Set green text for normal operation
        print("\033[1;32;40m")
        # Return user to password menu
        passwordMenu()
    else:

    # Call the generatePassword function and pass in the user's choices
    # and display the return value to the user
        print('===========================================================') 
        print('| Generating Password .................                   |') 
        print('===========================================================') 
        print("Your new password is: " + generatePassword
        (length,upper,lower,numbers,symbols))
        print('===========================================================')
        #return user to main menu
        menu()

def generatePassword(length,upper,lower,numbers,symbols):
    """function to use the data collected from user to generate a password"""

    # Create local variables for the set of characters that can be used
    # and the new password that will be returned from the function
    chars = ""
    newPassword = ""

    # Use if statements and the string.ascii_ constants to add the various
    # character sets to the local variable tracking what characters to be
    # used 
    upper = bool(upper)
    lower = bool(lower)
    numbers = bool(numbers)
    symbols = bool(symbols)
    if upper == True:
        chars = string.ascii_uppercase
    if lower == True:
        chars = chars + string.ascii_lowercase
    if numbers == True:
        chars = chars + string.digits
    if symbols == True:
        chars = chars + string.punctuation
    
    # Create a loop to add a random character from the set of
    # characters (hint: using random.choice(...)) to the new password
    # placeholder variable
    counter = 0
    while counter < length:
        newPassword = newPassword + random.choice(chars)
        counter = counter + 1
    # Showing the values the user selected
    print ("Your password length is " + str(length))
    print ("Your password may contain UPPERCASE:" + str(upper))
    print ("Your password may contain lowercase: " + str(lower))
    print ("Your password may contain numbers: " + str(numbers))
    print ("Your password may contain symbols: " + str(symbols))
    # Return the new password as the function's return value
    return newPassword


def encryptMessage(plaintext, key):
    """Function to encrypt the message."""
    # Create a placeholder variable to store the ciphertext
    ciphertext = ""

    # Work through each character in the message.
    for char in plaintext:
        # Each character will be replaced by its match
        # in the key variable.
        # Symbols and special characters will not be encrypted.
        if alphabet.find(char) > -1:
            ciphertext += key[alphabet.find(char)]
        else:
            ciphertext += char
    
    # Returns the encrypted text
    return ciphertext




def decryptMessage(ciphertext, key):
    """Function to decrypt the message."""
    # Crea=e a placeholder variable to store the plaintext
    plaintext = ""
    
    for char in ciphertext:
        if alphabet.find(char) > -1:
            plaintext += alphabet[key.find(char)]
        else:
            plaintext += char
    
    
    # Return the decrypted text
    return plaintext

def encrypt():
    '''This functions collects the user data to encrypt'''
    # Print a welcome message
    print('===========================================================')
    print('  _______                     ____     _____               ') 
    print(' |__   __|                   |___ \   |_   _|              ')
    print('    | | ___  __ _ _ __ ___     __) |    | |  _ __   ___    ')
    print('    | |/ _ \/ _` | \'_ ` _ \   |__ <     | | | \'_ \ / __|   ')
    print('    | |  __/ (_| | | | | | |  ___) |   _| |_| | | | (__ _  ')
    print('    |_|\___|\__,_|_| |_| |_| |____( ) |_____|_| |_|\___(_) ')
    print('                                  |/                       ')
    print('===========================================================') 
    print('==================  Message Encryption  ===================') 
    print('===========================================================') 
    print("Remember special characters,numbers and upper case letters")
    print("will not be encrypted!")
    print("")
    print("Please make your message between 1 and 20 characters.")
    message = input("Type a message to encrypt: ")
    if  len(message) < 1 or len(message) > 20:
        #Set red text for error message
        print("\033[1;31;40m")
        print('===========================================================') 
        print('| The message is not the proper length!                   |') 
        print('===========================================================') 
        #Set green text for normal operation
        print("\033[1;32;40m")
        # return to beginning of function so they can try again
        encrypt()
    else:
        encrypted = encryptMessage(message, key)
        print("Your encrypted message is: " + encrypted)

    #return to main menu    
    menu()

def decrypt():
    '''This fucntion decrypts the users input.'''
    # Print a welcome message
    print('===========================================================')
    print('  _______                     ____     _____               ') 
    print(' |__   __|                   |___ \   |_   _|              ')
    print('    | | ___  __ _ _ __ ___     __) |    | |  _ __   ___    ')
    print('    | |/ _ \/ _` | \'_ ` _ \   |__ <     | | | \'_ \ / __|   ')
    print('    | |  __/ (_| | | | | | |  ___) |   _| |_| | | | (__ _  ')
    print('    |_|\___|\__,_|_| |_| |_| |____( ) |_____|_| |_|\___(_) ')
    print('                                  |/                       ')
    print('===========================================================') 
    print('==================  Message Decryption  ===================') 
    print('===========================================================') 
    print("Remember only messages encypted within our network")
    print("will be decrypted!")
    print("")
    message_decrypt = input("Type the message to decrypt:")
    decrytped = decryptMessage(message_decrypt, key)
    print("Your decrypted message is: " + decrytped)
    menu()

def team():
    """function to display the developers of the app"""
# Print credits for the application and return to menu
    print('===========================================================')
    print('  _______                     ____     _____               ') 
    print(' |__   __|                   |___ \   |_   _|              ')
    print('    | | ___  __ _ _ __ ___     __) |    | |  _ __   ___    ')
    print('    | |/ _ \/ _` | \'_ ` _ \   |__ <     | | | \'_ \ / __| ')
    print('    | |  __/ (_| | | | | | |  ___) |   _| |_| | | | (__ _  ')
    print('    |_|\___|\__,_|_| |_| |_| |____( ) |_____|_| |_|\___(_) ')
    print('                                  |/                       ')
    print('===========================================================') 
    print('================ Security Application 1.0 =================') 
    print('===========================================================') 
    print('| This application was developed by our talented team.    |') 
    print('|                                                         |') 
    print('| Michael Markwood - S01225355                            |') 
    print('| Oluwatomisin Fayomi - S01248177                         |') 
    print('| Michael Kupresanin - S00052721                          |') 
    print('| Eric Oldag - S00635901                                  |') 
    print('| Leinaliz Martinez - S01063127                           |') 
    print('|                                                         |') 
    print('|A special THANK YOU to Professor Crowley for his guidance|') 
    print('===========================================================') 
    menu()

def exit():
    """function to exit the app and show credits first"""
# Print credits for the application and exit
    print('===========================================================')
    print('  _______                     ____     _____               ') 
    print(' |__   __|                   |___ \   |_   _|              ')
    print('    | | ___  __ _ _ __ ___     __) |    | |  _ __   ___    ')
    print('    | |/ _ \/ _` | \'_ ` _ \   |__ <     | | | \'_ \ / __| ')
    print('    | |  __/ (_| | | | | | |  ___) |   _| |_| | | | (__ _  ')
    print('    |_|\___|\__,_|_| |_| |_| |____( ) |_____|_| |_|\___(_) ')
    print('                                  |/                       ')
    print('===========================================================') 
    print('================ Security Application 1.0 =================') 
    print('===========================================================') 
    print('| This application was developed by our talented team.    |') 
    print('|                                                         |') 
    print('| Michael Markwood - S01225355                            |') 
    print('| Oluwatomisin Fayomi - S01248177                         |') 
    print('| Michael Kupresanin - S00052721                          |') 
    print('| Eric Oldag - S00635901                                  |') 
    print('| Leinaliz Martinez - S01063127                           |') 
    print('|                                                         |') 
    print('|A special THANK YOU to Professor Crowley for his guidance|') 
    print('===========================================================') 
    print("\033[1;36;40m")
    print('         ______                 _ _                 _      ')
    print('        / _____)               | | |               | |     ')
    print('       | /  ___  ___   ___   _ | | | _  _   _  ____| |     ')
    print('       | | (___)/ _ \ / _ \ / || | || \| | | |/ _  )_|     ')
    print('       | \____/| |_| | |_| ( (_| | |_) ) |_| ( (/ / _      ')
    print('        \_____/ \___/ \___/ \____|____/ \__  |\____)_|     ')
    print('                                       (____/              ')
    #Exit the app
    sys.exit()


def menu():
    """Function to display a menu for the app and prompt for input"""
    # Print a menu for the application
    print('===========================================================')
    print('  _______                     ____     _____               ') 
    print(' |__   __|                   |___ \   |_   _|              ')
    print('    | | ___  __ _ _ __ ___     __) |    | |  _ __   ___    ')
    print('    | |/ _ \/ _` | \'_ ` _ \   |__ <     | | | \'_ \ / __| ')
    print('    | |  __/ (_| | | | | | |  ___) |   _| |_| | | | (__ _  ')
    print('    |_|\___|\__,_|_| |_| |_| |____( ) |_____|_| |_|\___(_) ')
    print('                                  |/                       ')
    print('===========================================================') 
    print('================ Security Application 1.0 =================') 
    print('===========================================================') 
    print('|Please choose from the following options:                |') 
    print('|                                                         |') 
    print('|1 - Password Generation                                  |') 
    print('|2 - Message Encryption                                   |') 
    print('|3 - Message Decryption                                   |') 
    print('|4 - Application Credits                                  |') 
    print('|5 - Exit                                                 |') 
    print('===========================================================') 
    choice = input("What is your selection? ")
    print("")
    print("")

    # Option 1 - Send user to the Password function
    if choice == "1":
        passwordMenu() 

    # Option 2 - Encrypt Function
    elif choice == "2":
        encrypt()

    # Option 3 - Decrypt Function
    elif choice == "3":
        decrypt()

    # Option 4 - Send user to the Team function
    elif choice == "4":
        team()

    # Option 5 - Send user to the Exit function
    elif choice == "5":
        exit()

    #Output for wrong choice
    else:
        #Set red text for error message
        print("\033[1;31;40m")
        print("That is not a valid option! ")
        #Set green text for normal operation
        print("\033[1;32;40m")
        #Reload the menu
        menu()

#Load the menu
menu()
