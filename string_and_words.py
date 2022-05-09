# -*- coding: utf-8 -*-
"""
Created on Sun May  8 14:17:32 2022

@author: DiegoAlducin
"""

# Initializing the program and Main function
#############################################

def main():
    '''main program'''
    print("\n")
    print('String stats and replacements')
    print('=========================\n')
    print("Enter (1) if file will be read from directory, must be .txt file")
    print("Enter (2) if string will be entered.")
    file_select = input()

    # Reading file name from directory
    if file_select == '1':
        print("\nEnter file name")
        file_name = input()
        text_file = open(file_name, 'r', encoding="utf8")
        #with open(file_name, 'r', encoding="utf8") as text_file:
        text = text_file.read()
    # Text to be read is String entered.
    elif file_select == '2':
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
    print("Enter (3) to use grepline (return line with keyword).")
    requirement_select = input()

    # Logic to pick which requirement is to be tested

    ## REQUIREMENT 1
    if requirement_select == '1':
        words = text_cleaner(text)
        unique, unique_counter = unique_word_stats(words)
        stat_printer(unique, unique_counter)

    ## REQUIREMENT 2
    elif requirement_select == '2':
        print("Enter old word to be replaced: ")
        old_word = input()
        print("\n")

        print("Enter word that will replace old word: ")
        new_word = input()
        new_text = replace_words(text, old_word, new_word)
        print("\n")

        print("NEW TEXT:\n")
        print(new_text)

    elif requirement_select =='3':
        print("Enter keyword to search: ")
        keyword = input()
        grepline(text_file, keyword)


#   AUXILIARY FUNCTIONS
#######################

# Text cleaner and normalizer
# ===========================
# input: (text) text string
# output: (words) word list in array
def text_cleaner(text):
    '''text_cleaner: cleans and normalizes words in text'''
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
# output: (unique) unique words dictionary, (unique_counter) unique word counter
def unique_word_stats(words):
    '''unique_word_stats: calculates words statistics in text'''
    unique = {}
    unique_counter = 0
    for word in words:
        if word not in unique:
            unique_counter += 1
            unique[word] = 0
        unique[word] += 1
    return unique, unique_counter

# Prints unique word stats
# ========================
# input: (unique) unique word dictionary, (unique_counter) integer unique word count
# output: prints unique word count and word with each count
def stat_printer(unique, unique_counter):
    '''stat_printer: prints document statistics'''
    # sort dictionary
    sorted_unique = sorted(unique.keys())
    # Print words
    print("\n")
    print("Number of unique words : ", unique_counter)
    print("============================")
    for word in sorted_unique:
        print(word, ':', unique[word])

# Replaces word from text returns text
# ====================================
# input: (text) text String, (old_word) oldWord string, (new_word) new word string
# output: returns text with newWord where replaced oldWord
def replace_words(text, old_word, new_word):
    '''replace_words: replaces old_word with new_word in text'''
    return text.replace(old_word, new_word)

# Grepline
# ========
# input: (text) text String, (keyword) String keyword to be searched
# output:  Returns and prints line where keyword was found
def grepline(text_file, keyword):
    '''grepline: finds keyword in line of text'''
    text_file.seek(0,0) # returns cursor back to beginning of file
    lines = text_file.readlines()
    line_count = 0
    print("\nKeyword found in the following lines:\n")
    for line in lines:
        if keyword in line:
            print(f'Line {line_count}: {line}')
        line_count += 1
    print("End of file.")

# RUNS MAIN PROGRAM (in loop)
###################
while True:

    main()
    print("\n")
    print("Want to run program again? (Y/N)")
    yes_no = input()

    if yes_no == 'y':
        continue

    print("\n")
    print("Goodbye.")
    print("Created by Diego Alducin, zrf055")
    break
    