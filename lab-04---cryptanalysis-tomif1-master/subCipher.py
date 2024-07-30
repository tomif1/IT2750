######################################
# IT 2750 - Lab 4                    #
# Substitution Ciphers               #
# Author: Oluwatomisin Fayomi        #
######################################

# Store the alphabet and the key that corresponds to
# each character in the substitution
alphabet = "abcdefghijklmnopqrstuvwxyz"
key      = "zjrekydnqoluaxmicvpgtfbhws"

# Function decryptMessage
# Decrypt a message using a key and output plaintext
# Parameters:
# - ciphertext -> string, message to decrypt
# - key -> string, key to use in substitution cipher
# Returns:
# - string, decrypted message
def decryptMessage(ciphertext, key):
    # Create a placeholder variable to store the plaintext
    plaintext = ""

    ##############################################
    ####  REPLACE THIS BLOCK WITH YOUR CODE  #####
    ##############################################
    for char in ciphertext:
        if key.find(char) > -1:
            plaintext += alphabet[key.find(char)]
        else:
            plaintext += char
    
    # Return the decrypted text
    return plaintext

# Function encryptMessage
# Encrypt a message using a key and output ciphertext
# Parameters:
# - plaintext -> string, message to encrypt
# - key -> string, key to use in substitution cipher
# Returns:
# - string, encrypted message
def encryptMessage(plaintext, key):
    # Create a placeholder variable to store the ciphertext
    ciphertext = ""


    # Iterate through each character in the plaintext message
    for char in plaintext:
        # If the character is in the alphabet, replace the
        # character in the alphabet with the corresponding
        # character in the key and add it to the ciphertext.
        # If it is not (find returns -1), add the character
        # as-is (space, uppercase letter, symbol, etc.)
        if alphabet.find(char) > -1:
            ciphertext += key[alphabet.find(char)]
        else:
            ciphertext += char
    
    # Return the encrypted text
    return ciphertext

# Grab a message from the user
message = input("Type a message to encrypt: ")

# Encrypt the message and save in a variable
encrypted = encryptMessage(message, key)

# Decrypt the message and save in a variable
decrypted = decryptMessage(encrypted, key)

# Output the original message, the encrypted message, and
# the decrypted message. The original message and the
# decrypted message should match!
print("Plaintext message: " + message)
print("Encrypted message: " + encrypted)
print("Decrypted message: " + decrypted)
