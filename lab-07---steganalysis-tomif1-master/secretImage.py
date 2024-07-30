##########################################
#### IT 2750 - Lab 07                    #
#### Steganography                       #
#### Author: Oluwatomisin Fayomi         #
##########################################

from turtle import width
from PIL import Image

def stringToBits(string):
    return str(bin(int.from_bytes(string.encode(), 'big')))[2:]

def bitsToString(bits):
    if bits[0:2] != '0b':
        bits = '0b' + bits
    value = int(bits, 2)
    return value.to_bytes((value.bit_length() + 7) // 8, 'big').decode()

def writeMessageToRedChannel(file, message):
    image = Image.open(file)
    width, height = image.size
    messageBits = stringToBits(message)
    messageBitCounter = 0
    y = 0
    while y < height:
        x = 0
        while x < width:
            r, g, b, a = image.getpixel((x, y))
            print("writeMessageToRedChannel: Reading pixel %d, %d - Original values (%d, %d, %d, %d)" % (x, y, r, g, b, a))
            if(messageBitCounter < len(messageBits)):
                r = int(messageBits[messageBitCounter])
            else:
                r = 255
            print("writeMessageToRedChannel: Editing pixel %d, %d - New values (%d, %d, %d, %d)" % (x, y, r, g, b, a))
            image.putpixel((x,y), (r, g, b, a))
            x += 1
            messageBitCounter += 1
        y += 1
    image.save(file)

def readMessageFromRedChannel(file):
    image = Image.open(file)
    width, height = image.size
    message = ""
    y = 0
    while y < height:
        x = 0
        while x < width:
            r, g, b, a = image.getpixel((x, y))
            if(r != 255):
                message += str(r)
            else:
                return bitsToString(message)
            x += 1
        y += 1

#########################################
### EDIT CODE BELOW THIS COMMENT ########
#########################################

def resetImage(file):
    # Open the Image specified in file
    image = Image.open(file)
    # Get the width and height
    width, height = image.size
    # Write a nested loop statement to access each pixel
    y = 0
    while y < height:
        x = 0
        while x < width:
    
        
        
            # Get the current pixel RGBA
            r, g, b, a = image.getpixel((x,y))
            # Print the current value to the screen
            print("Changing pixels ({0}, {1})".format(x,y))
            print("Old Values = ({0}, {1}, {2}, {3})".format(r, g, b, a))
            #print("R = %d, G = %d, B = %d, A = %d," % r, g, b, a)
            # Write new RGBA of (255, 255, 255, 255) to the pixel
            image.putpixel((x,y),(255,255,255,255))
            # Print the new value ,to the screen
            r,g,b,a = image.getpixel((x,y))
            print("New Values = ({}, {}, {}, {})".format(r,g,b,a))
            x+=1
        y+=1
            
        
    # Save the image file
    image.save(file)

#########################################
### EDIT CODE ABOVE THIS COMMENT ########
#########################################

message  = "Hello, there! How are you! I want to tell you a secret... "
message += "and the secret is that I am Batman!!!"

# Reset the image to all white pixels
# RGBA = (255, 255, 255, 255)
resetImage("secret_image.png")

# Write message to the image
print("Writing the secret message: %s" % message)
writeMessageToRedChannel("secret_image.png", message)

# Read message from the image (if it worked properly, the
# message should be the same as the one written to the image)
print("Reading the secret message: %s" % readMessageFromRedChannel("secret_image.png"))
