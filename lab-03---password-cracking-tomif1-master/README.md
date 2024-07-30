# IT 2750 - Lab 03
___
#### Your Name: Oluwatomisin Fayomi
#### S-Number: S01248177
___
### Assignment Description
This week, we will be creating and running a Python script that cracks a password-protected zip file using passwords defined in a list. Your program will be able to crack the week3data.zip ZIP file that is included along with the assignment. If the code works properly, you will extract the Tri-C Triceratops logo as a JPG file from the ZIP.
### Lab Steps
You will perform the following steps to complete the Week 1 lab:
1. Fetch the repository for the assignment and update your Name and S-Number in the Readme.md file
2. Review the crackZip.py file and read the comments. Take note of the areas where I ask you to write or modify the code.
3. Watch the lab video (optional) if you would like some suggestions on how to go about this lab
4. Grab a Mountain Dew and write some code!
5. Test your code. USE THE week3data.zip ZIP file to test your code. Watch the video for an example, but when extracted properly there should be a JPG file of the Triceratops logo. Go back to Step 4 if something doesn't work.
6. Commit, push, and take a break!
### Lab Requirements
1. Create a list variable and initialize it with the first 10 of the top 25 most used passwords in 2019, per the following link https://en.wikipedia.org/wiki/List_of_the_most_common_passwords . USE THE FIRST TABLE, "According to SplashData"
2. Ask the user for the filename of the zip file that we will attempt to crack (just the filename, not the full path... make sure the actual zip file is in the same directory as the python script and that the current working directory in the command prompt is that same directory)
3. Create a loop that iterates through each password in the list. You can use a while loop or for loop
4. For each iteration of the loop, attempt to crack the zipfile password by calling the openZip function and passing the filename and the password to try. The openZip function returns True if it was successful and False if it was not
5. For each iteraton of the loop, let the user know what the result of the crack attempt was (True = success, False = failure) and what password was tried
### Lab Rubric
The lab will be graded using the following rubric. Total 10 points for the assignment.

| Rubric Item | Novice | Competent | Proficient |
|:---------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------:|
| Submission Expectations (max 1pt) | Project was not committed to GitHub  (0-0.5pt) | Project was partially committed to GitHub (0.5-1pt) | Project was fully committed to GitHub (1pt) |
| Functional Expectations (max 9pt) | The code does not function nor does it follow all instructions. There are significant errors and the program cannot be run. Student did not adhere to the assignment. (0-6pt) | Most instructions were followed and there may or may not be an error that prevents the application from running. Student generally adhered the assignment. (6-9pt) | Instructions were followed. Code was well commented and understandable. There are no errors and the application runs as expected. (9pt) |
