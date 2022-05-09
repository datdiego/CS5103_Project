# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:46:21 2022

@author: Diego Alducin
"""

import string_and_words
import unittest

class test_main(unittest.TestCase):
    """
    Test the functions from main program.
    """


    def test_unique_word_stats(self):
        """
        Testing unique_word_stats from main.py, checking both texts if they are equal
        """
        # Test strings and solutions for unique_word_stats function
        
        stats_test_text = "one"
        stats_test_solution = ({'o': 1, 'n': 1, 'e': 1}, 3)
        
        self.assertEqual(string_and_words.unique_word_stats(stats_test_text), stats_test_solution)
        
 
    def test_replace_words(self):
        """
        Testing replace_words from main.py, checking both texts are equal after replacement
        """
        
        test_text_replace_file = open('data.txt', 'r', encoding="utf8")
        test_text_replace = test_text_replace_file.read()
        test_text_replace_solution_file = open('replace_solution.txt', 'r', encoding="utf8")
        test_text_replace_solution = test_text_replace_solution_file.read()
         
        self.assertEqual(string_and_words.replace_words(test_text_replace, 'program', 'application'), test_text_replace_solution)
        
        test_text_replace_file.close()
        test_text_replace_solution_file.close()
        
    def test_grepline(self):
        """
        Testing grepline, which checks if correct line was returned from word searched.
        """
        
        test_text_grepline_file = open('data.txt', 'r', encoding="utf8")
        test_text_grepline_solution = None
        test_string_results = string_and_words.grepline(test_text_grepline_file, 'first')
        
        self.assertEqual(test_string_results, test_text_grepline_solution)
        
        test_text_grepline_file.close()