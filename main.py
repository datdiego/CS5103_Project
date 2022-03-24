# Main program
# ============
#
#   1st Requirement:    Count the frequency of each unique word.
#                       Must support the combinations of space, tab, and new line character as separators
#                
#   2nd Requirement:    Whole word replacement.
#



# Initializing the program and Main function
#############################################

def main():
    print('Text File Word Statistics')
    print('=========================\n')
    print("Enter (1) if file will be read from directory, must be .txt file")
    print("Enter (2) if string will be entered.")
    fileSelect = input()
    
    # Reading file name from directory
    if fileSelect == '1':
        print("\nEnter file name")
        fileName = input()
        text_file = open(fileName, 'r')
        text = text_file.read()
    # Text to be read is String entered.
    elif fileSelect == '2':
        print("Enter String:")
        text = input()
        
    # PRINT TEXT
    print("TEXT:\n")
    print(text)
    
    # Select the requirement
    print("\n")
    print("Select the requirement to test:")
    print("===============================\n")
    print("Enter (1) if UNIQUE word frequency is to be tested")
    print("Enter (2) if a whole word will be REPLACED.")
    requirementSelect = input()
    
    # Logic to pick which requirement is to be tested
    
    ## REQUIREMENT 1
    if requirementSelect == '1':
        words = textCleaner(text)
        unique, uniqueCounter = uniqueWordStats(words)
        statPrinter(unique, uniqueCounter)
    
    ## REQUIREMENT 2
    elif requirementSelect == '2':
        print("Enter old word to be replaced: ")
        oldWord = input()
        print("\n")
        
        print("Enter word that will replace old word: ")
        newWord = input()
        newText = replaceWords(text, oldWord, newWord)
        print("\n")
        
        print("NEW TEXT:\n")
        print(newText)
        
    return
    

#   AUXILIARY FUNCTIONS
#######################

# Text cleaner and normalizer
# ===========================
# input: (text) text string
# output: (words) word list in array
def textCleaner(text):
    # Normalizes the words to lower case for easier counting
    text = text.lower()

    # Splits the words from space, tab or new line characteres
    words = text.split()

    # Cleans and removes 
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]
    
    return words



# Finding unique word stats
# =========================
# input: (words) word list in array
# output: (unique) unique words dictionary, (uniqueCounter) unique word counter
def uniqueWordStats(words):
    unique = {}
    uniqueCounter = 0
    for word in words:
        if word not in unique:
            uniqueCounter += 1
            unique[word] = 0
        unique[word] += 1
    return unique, uniqueCounter


# Prints unique word stats
# ========================
# input: (unique) unique word dictionary, (uniqueCounter) integer unique word count
# output: prints unique word count and word with each count
def statPrinter(unique, uniqueCounter):
    # sort dictionary
    sortedUnique = sorted(unique.keys())
    # Print words 
    print("\n")
    print("Number of unique words : ", uniqueCounter)
    print("============================")
    for word in sortedUnique:
        print(word, ':', unique[word])
    return

# Replaces word from text returns text
# ====================================
# input: (text) text String, (oldWord) oldWord string, (newWord) new word string
def replaceWords(text, oldWord, newWord):
    return text.replace(oldWord, newWord)


# RUNS MAIN PROGRAM (in loop)
###################
while True:
    
    main()
    print("\n")
    print("Want to run program again? (Y/N)")
    yesNo = input()
    
    if yesNo == 'y':
        continue
    else:
        print("\n")
        print("Goodbye.")
        print("Created by Diego Alducin, zrf055")
        break
    