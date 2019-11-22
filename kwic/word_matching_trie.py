""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 2
   
    Problem 4: Keyword in Context.

    <Please insert your data and the honor code here.>
"""

from tries import StandardTrie


class WordMatchingTrie(StandardTrie):
    """Representation of a word-matching trie."""

    def __init__(self, text):
        """ Constructor for WordMatchingTrie. Builds the trie based on the supplied text.
        
        Parameters
        ----------
        text : string
            A text to be used for constructing the trie.
        """

        # FIXME your code goes here


    def add(self, string, value):
        """ Adds a new (string, value) pair to the trie. The value should be 
        the start index of the string in the text. It should be added to the
        node having the last letter of the string as a key. If a word appears
        multiple times in the text, the trie should store a list of the start
        indices as values.
        
        Parameters
        __________
        string : string
            The string to add to the trie.
        value : object
            A start index of the string in the text.
        """

        # FIXME your code goes here

    class Node(StandardTrie.Node):

        def __init__(self):
            """ Do not call this constructor directly. A node should have a key, a value and a dictionary of children. The _value attribute should be able to store multiple values for the same node."""

            # FIXME your code goes here


