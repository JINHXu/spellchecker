""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 2
   
    Problem 3: Spell checker using a trie.

    Course:      Data Structures and Algorithms for CL III - WS1920
    Assignment:  lab 2, exercise 3
    Author:      Jinghua Xu
    Description: A spell checker implemented with trie, i.e. lexicon will be stored in a trie instead of a set.
    Honor Code:  I pledge that this program represents my own work.
"""

class TrieSpellChecker:

    def __init__(self, lexicon):
        self._lexicon = StandardTrie(lexicon)


    @property
    def lexicon(self):
        return self._lexicon

    def check(self, word):
        spellings = []

        # FIXME your code goes here

        return spellings
