#!/usr/bin/env/python3

""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 2
   
    Problem 4: Keyword in Context

    Assignment:  lab 2, exercise 4
    Author:      Jinghua Xu
    Description: an interface for visualizing keywords in context using tries
 
    Honor Code:  I pledge that this program represents my own work.
"""

from kwic.word_matching_trie import WordMatchingTrie

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KWIC app")
    parser.add_argument("-f", "--file", type=argparse.FileType(mode="r", encoding="utf-8"), default="kwic/data/2701-0.txt")
    parser.add_argument("-w", "--window-size", type=int, default=50)
    parser.add_argument("-m", "--max-count", type=int, default=10)
    # key word to search 
    parser.add_argument("-k", "--keyword", type=str, default='')
    args = parser.parse_args()

    text = ''
    # read from file
    with args.file as file:
        for line in file:
            # remove any newlines from the text
            text += line.strip('\n')

    # trie to store text
    trie = WordMatchingTrie(text)

    keyword = args.keyword
    w_sz = args.window_size

    # The program should keep asking for a new keyword until the user terminates the loop by presses enter without inputting any characters.
    while True:
        values = trie.find(keyword) 
        len_keyword = len(keyword) 
        # query the text for the keyword
        if values:
            # it should print the args.max_count contexts for the word
            values = values[:args.max_count]
            for idx in values:
                # args.w chars(including spaces) to the left of keyword
                context_to_left = text[idx-w_sz: idx]
                # args.w chars(including spaces) to the right of keyword
                context_to_right = text[idx+len_keyword: idx+len_keyword+w_sz]
                # left justification of suceeding context(optional line of code, depending on requirement, which is vague here)
                # context_to_right = context_to_right.lstrip()
                # right justification of preceding context(optional line of code, depending on requirement, which is vague here)
                # context_to_left = context_to_left.rstrip()
                # In cases where the contexts are smaller than window_sz
                if len(context_to_left) < args.window_size:
                    #right justification of preceding context
                    num_spaces = args.max_count - len(context_to_left)
                    print(' '*num_spaces + context_to_left + ' '*4 + keyword + ' '*4 + context_to_right)
                else:
                    print(context_to_left + ' '*4 + keyword + ' '*4 + context_to_right)

        else:
            print('Keyword not found in text.')
        
        nextcommand = input("Enter new keyword to search or press Enter to terminate:")

        if nextcommand == '':
            break
        else:
            keyword = nextcommand

        
            
    
