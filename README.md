# CS5103 Software Engineering : Course Project
Diego Alducin, zrf055

Professor: Xiaoyin Wang

CheckPoint: 3/24/2022

Language: Python3

Final: 5/8/2022

#### Version 0.2

### TEST CASE 1

TEST CASE DESCRIPTION
1. Input a string or text document into program.
2. The program returns the count frequencey of each unique word.
3. It should be able to read across spaces, tabs, and newline characters as separators.

TEST DATA

Input: 
String:	Hello World

EXPECTED RESULTS

Output: 
		hello: 1
		world: 1

### TEST CASE 2
1. Input a string or text document into program.
2. Enter a old word from the strin or text document to be replaced.
3. Replace the old word with a new input word within the string or text document.
4. Print string or text document with new word.

TEST DATA

Input: 
String: 	Hello World
Old Word:	Hello
New Word:	Hi

EXPECTED RESULTS

Output:
		Hi World

### TEST CASE 3
1. New feature called grepline.
2. Input a text document into program.
3. Input a keyword into program.
4. Program will search the document by line and returns the line in which the word was found.

TEST DATA

Input:
Document:	Hello World.txt
		Hello World
		Hi Moon
Keyword:	World

EXPECTED RESULTS

Output:
	Line 0 : Hello World
## How to run program
### On Shell
1. Change directory to where 'main.py' is located. (Make sure Python3 is installed)
2. Enter 'python3 main.py' on shell to run python file.
3. The program will initialize and there are two options:
   - Option (1) Select file to read from directory, one file already provided to test requirement 'data.txt'/
   - Can only read '.txt' files.
   - Option (2) Enter String to be analyzed by program.
4. The TEXT from past selection will print.
5. The program will give two options to start either requirements:
   - Option (1) will provide unique word statistics from the TEXT.
   - Option (2) will replace an old word from the text to a new word from user input.
6. Program will ask if user wants to restart program.
