# GPTaskAutomator

This script utilizes the GPT model using the OpenAI API to generate, and EXECUTE Python code to do user defined tasks.

## Prerequisites

To run the script, you need to specify in the config.ini file a valid OpenAI API key (you can obtain this from the OpenAI platform).

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies specified in the requirements.txt file

## Examples of usage

- You can declare: "Move the files in the path "PATH_OF_DIRECTORY" in subfolders named with their initial letter." to let the program organize files for you.
- You can declare: "Create a csv file containing the list of all the files found in the path "PATH_OF_DIRECTORY" and their respective file size in KB." to let the program do it for you.

## Disclaimer
Be careful to what type of tasks and how you specify them. 
The program can execute potentially dangerous operation based on what or how you declare the action to perform.
Some of potentially dangerous tasks can be the deletion of unwanted files, or changing some configuration or your device.
Remember also to not share personal information about you, and that everything you write is subjected to OpenAI use policies.
I am not responsible for a bad use of the program.
