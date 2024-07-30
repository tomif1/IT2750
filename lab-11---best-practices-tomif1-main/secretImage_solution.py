  ### 10 comm3nts
##########################################
#### IT 2750 - Week 12 Lab               #
#### Python Best Practices               #
#### Author: Oluwatomisin Fayomi         #
##########################################

from PIL import Image

def stringToBits(string):
    """Converts a String to bits of data."""
    
    # Convert the string to bytes, then bits, then take those
    # bits and turn them into a string
    return str(bin(int.from_bytes(string.encode(), 'big')))[2:]

def bitsToString(bits):
    """Converts a Bit to a string of data."""

    # If bit 0 trhough 2 do not equal 0b add make bits equal
    # 0b plus bits
    if bits[0:2] != '0b':
        bits = '0b' + bits
    value = int(bits, 2)

    # Return the value 
    return value.to_bytes((value.bit_length() + 7) // 8, 'big').decode()

def writeMessageToRedChannel(file, message):
    """Writes the secret message to the Image file."""

    # Opens the image file of the string path provided    
    image = Image.open(file)
    
    # Gets the height and width values from
    # the image and stores them        
    width, height = image.size

    # Converts the message value to bits and stores it in 
    # messageBits
    messageBits = stringToBits(message)

    # Reset the message Bit counter
    messageBitCounter = 0
    y = 0
    while y < height:
        x = 0
        while x < width:
            r, g, b, a = image.getpixel((x, y))
            # Prints the current of r,g,b,a values of the pixel 
            # we are currently viewing
            print(
               "writeMessageToRedChannel:"
               + " Reading pixel %d, %d - Original values (%d, %d, %d, %d)" 
               % (x, y, r, g, b, a)
            )
            # Sets r to the integer of messageBits when 
            # messageBitCounter is less than the length 
            # of messageBits
            if(messageBitCounter < len(messageBits)):
                r = int(messageBits[messageBitCounter])
            else:
                r = 255
            print("writeMessageToRedChannel: "
             + "Editing pixel %d, %d - New values (%d, %d, %d, %d)" 
               % (x, y, r, g, b, a)
               )
            image.putpixel((x,y), (r, g, b, a))
            x += 1
            messageBitCounter += 1
        y += 1
    image.save(file)

def readMessageFromRedChannel(file):
    """Read the message written to the Image file."""

    image = Image.open(file)
    width, height = image.size
    
    # Resets the message value
    message = ""

    # Resets the y axis
    y = 0

    while y < height:
        # Resets the x axis
        x = 0
        while x < width:
            r, g, b, a = image.getpixel((x, y))
            
            # If the value of is not 255, add it to message
            # as a string
            if(r != 255):
                message += str(r)

            # If not convert the message input to a string
            else:
                return bitsToString(message)
            x += 1
        y += 1

def resetImage(file):
    """Resets the Image file provided all to white"""

    image = Image.open(file)
    width, height = image.size

    x = 0
    while x < width:
        y = 0
        while y < height:

            # Gets the rgba color codes from the pixel 
            # provided and stores them in those values
            r, g, b, a = image.getpixel((x, y))
            print("resetImage: " + "Reading pixel %d, %d - Old values (%d, %d, %d, %d)" % (x, y, r, g, b, a))

            # Sets the same pixels as above color values
            # to 255, making it white
            image.putpixel((x,y), (255, 255, 255, 255))
            print("resetImage: " + "Editing pixel %d, %d - New values (%d, %d, %d, %d)" % (x, y, 255, 255, 255, 255))
            
            # Moves down one pixel
            y += 1
        # After all of the y pixels in that column have 
        # their color changed it moves over one pixel
        # and starts over.
        x += 1
    
    # Saves the file image to the string value
    #  of the path provided.
    image.save(file)

message  = "Hello, there! How are you! I want to tell you a secret... "
message += "and the secret is that I am Batman!!!"
resetImage("secret_image.png")
print("Writing the secret message: %s" % message)
writeMessageToRedChannel("secret_image.png", message)
print("Reading the secret message: %s" % readMessageFromRedChannel("secret_image.png"))
