# File Generator Python Project
A python command-line script that allows the user to change multiple aspects of the files they want to generate.

## Overview
This python project takes 4 inputs from the user,
- File Name
- Number of Files
- File Extension
- A message to be viewable inside the file.

A json file is also contained with this project to show you your previous result and save your inputs after the script quits. 

`{"FileName": "testfile", "NumOfFiles": 10, "FileExtension": "txt", "CustomMessage": "This is a Custom Message."}`


## Requirements
Python 3.8 and above
Access to a terminal/IDE with a terminal.
Permission to create files

## How to Use

### Specific Commands for the Script
**python main.py 'File Name' 'Number of Files' 'File Extension' 'Custom Message'**

let's you quickly customise the file(s) you want to generate.

**python main.py viewJson**

Let's you view your Json settings

**Python main.py reset**

Resets to default values.

**Python main.py previous**

Outputs the previous inputs and lets you output them quicker

**Python main.py help**

Gives a more simplified version of this 'how to use' page.


## How I used AI
For this project, I used AI to help me debug and fix my code with the help of Github Copilot. I made sure to proof-read any AI fix to guarantee that it didn't introduce extra bugs within my code and that it's implementation of code that I'm able to understand myself.