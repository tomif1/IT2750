##########################################
#### IT 2750 - Lab 08                    #
#### Web Scraping                        #
#### Author: Oluwatomisin Fayomi         #
##########################################

import requests, bs4, re

# Request page http://catalog.tri-c.edu/about/important-phone-numbers
# and call raise_for_status on the request object
res = requests.get('http://catalog.tri-c.edu/about/important-phone-numbers') # <--- FILL THIS LIST IN! (1pt)
# <-- CALL raise_for_status on res (1pt)

# Parse the text from the request object into a BeautifulSoup
# object using the 'html.parser'
catalogPage = bs4.BeautifulSoup(res.text, 'html.parser')

# Create a list of class selectors representing <td> classes
# used on the webpage that contain phone numbers
selectors = ['.column0', '.column1', '.column2', '.column3', '.column4']  # <--- FILL THIS LIST IN! (1pt)

# Iterate through each selector
for selector in selectors:
  
  # Select all elements for the current selector
  elements = catalogPage.select('.column1', '.column2','.column3', '.column4')  # <--- FILL IN THE CORRECT ARGUMENT (1pt)
  
  # Iterate through each element
  for element in elements:
  
    # Compile a regular expression for finding a phone number
    phoneRegex = re.compile(r'[0-9][0-9][0-9]\-[0-9][0-9][0-9]\-[0-9][0-9][0-9][0-9]')# <--- USE REGEX COMPILE (1pt)
    
    # Search for the phone number in the element's text
    text = element.getText()
    match = re.match(phoneRegex,text)# CALL THE SEARCH FUNCTION AND SAVE INTO VARIABLE MATCH (1pt)
    
    # If match == None, do nothing (continue)
    if match == None:
      continue
      
    #print the phone number to the screen
    print("Phone Number: ", match.string) # <--- ADD PHONE NUMBER HERE FOR DISPLAY (1pt)
