""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 2
   
    Problem 1: Spell checker.

    <Please insert your data and the honor code here.>
"""

class SpellChecker:
    """Class representing a spellchecker with a given lexicon."""

    def __init__(self, lexicon):
        """ Initializes the spell checker class by saving the user-provided lexicon.
        
        Parameters
        ----------
        lexicon : iterable
            An iterable collection of over the words that should be used as a dictionary for this spell checker.
        """
        self._lexicon = None

        # FIXME your code goes here

    @property
    def lexicon(self):
        return self._lexicon

    def check(self, word):
        """ Checks if a given string word is correctly spelled (i.e. if it is in the spell checker's lexicon). If the string is not in the lexicon, then it returns a list of potentially correct spellings of the word from the spell checker's lexicon.

        Parameters
        ----------
        word : string
            The string to be spell-checked.

        Returns
        -------
        spellings : list
            A list of correct/possible spellings of word. 
        """
        spellings = []

        # FIXME your code goes here

        return spellings
