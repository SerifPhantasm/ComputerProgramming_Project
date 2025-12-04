# File Generator Python Project
A python command-line script that allows the user to change multiple aspects of the files they want to generate.

## Overview
This python project takes 4 inputs from the user,
- File Name
- Number of Files
- File Extension
- A message to be viewable inside the file.

A json file is also contained with this project to show you your previous result and save your inputs after the script quits. 
## How it Works
When starting up, the script automatically creates a folder to put in all the files that you're wanting to create in the script (to be cleaner). If the folder already exists in the directory with the script, it skips creating it. The user is then prompted to give a name for the file, file extension and the amount of files you want to create. Lastly you're prompted to put in a message inside all the files you want the script to output. These values are then stored inside settings.json. There will be confirmation of the specific values that the user has inputted and if they've put in 'y', it will start printing

## Requirements
Python 3.8 and above
Access to a terminal/IDE with a terminal.
## How to Use

### Specific Commands for the Script
**python main.py 'File Name' 'Number of Files' 'File Extension' 'Custom Message'**

let's you quickly customise the file(s) you want to generate.

**python main.py viewJson**

Let's you view settings.json by outputting it in the terminal from main.py

**Python main.py reset**

Resets to default values.

**Python main.py previous**

Outputs the previous inputs and lets you output them quicker

**Python main.py help**

Gives a more simplified version of this 'how to use' page.


## How I used AI
For this project, I used AI to help me with debugging and fixing my code with the help of Copilot. I made sure to proof-read any AI fix to make sure that it didn't give me worse issues in my code and that it were fixes that I was able to understand myself.