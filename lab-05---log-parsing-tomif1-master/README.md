# IT 2750 - Lab 5
___
#### Your Name: Oluwatomisin Fayomi
#### S-Number: S01248177
___
### Assignment Description
This week, we will be be writing regular expressions that will match IP addresses and usernames in a Microsoft IIS log file. 
### Lab Steps
You will perform the following steps to complete the lab:
1. Fetch the repository for the assignment and update your Name and S-Number in the Readme.md file
2. Review the logRegEx.py file and read the comments. This program reads a log file and outputs all the unique IP addresses and username it finds within the file. Take note of the area where you will write your regular expressions. There are four places where you will make code changes. First, you will write a regular expression that matches IP addresses within the re.compile function call on line 36. Next, you will write a regular expression that matches usernames (in the format domain\username) on line 50. Finally, in steps 3 and 4 you will write a loop for each step that displays all the IP addresses (gathered into the list ipAddresses) and usernames (gathered in the list list users) to the console window.
3. Watch the lab video (optional) if you would like some suggestions on how to go about this lab
4. Grab a Mountain Dew and write some code!
5. Test your code. USE THE IIS.log file to test your code. Watch the video for an example, but when extracted properly there should be a JPG file of the Triceratops logo. Go back to Step 4 if something doesn't work.
6. Commit, push, and take a break!
### Lab Requirements
1. Write a valid regular expression that covers all IP addresses (line 36) - Up to 2.5pts under Functional Expectations
2. Write a valid regular expression that covers all usernames in the domain\user format (line 50) - Up to 2.5pts under Functional Expectations
3. Write a loop that displays all list items in the ipAddresses variable to the console window - Up to 1pts under Functional Expectations
4. Write a loop that displays all list items in the users variable to the console window - Up to 1pts under Functional Expectations
5. Ensure that your code runs without error - Up to 2pts under Functional Expectations
### Lab Rubric
The lab will be graded using the following rubric. Total 10 points for the assignment.

| Rubric Item | Novice | Competent | Proficient |
|:---------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------:|
| Submission Expectations (max 1pt) | Project was not committed to GitHub  (0-0.5pt) | Project was partially committed to GitHub (0.5-1pt) | Project was fully committed to GitHub (1pt) |
| Functional Expectations (max 9pt) | The code does not function nor does it follow all instructions. There are significant errors and the program cannot be run. Student did not adhere to the assignment. (0-6pt) | Most instructions were followed and there may or may not be an error that prevents the application from running. Student generally adhered the assignment. (6-9pt) | Instructions were followed. Code was well commented and understandable. There are no errors and the application runs as expected. (9pt) |
