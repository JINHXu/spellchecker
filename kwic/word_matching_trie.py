""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 2
   
    Problem 4: Keyword in Context.

    Assignment:  lab 2, exercise 4
    Author:      Jinghua Xu
    Description: an implementation of a word matching trie class
 
    Honor Code:  I pledge that this program represents my own work.
"""

import string
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

        self._root = self.Node()

        # text preocessing
        puncts = string.punctuation
        words_in_text = text.split(' ')
        value = 0
        for word in words_in_text:
            #removing puncts at the end of each string
            if word[-1] in puncts:
                word = word[:-1]
            self.add(word, value)
            value += len(word) + 1


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

        # current node
        node = self._root
        for char in string:
            found_in_child = False
            for child in node.children:
                if child.key == char:
                    found_in_child = True
                    node = child
                    break
            if not found_in_child:
                new_node = self.Node()
                new_node.key = char
                node.children[new_node] = new_node
                node = new_node
        node._value.append(value)

    class Node(StandardTrie.Node):

        def __init__(self):
            """ Do not call this constructor directly. A node should have a key, a value and a dictionary of children. The _value attribute should be able to store multiple values for the same node."""

            self._children = {}
            self._key = None
            self._value = []

def main():
    trie = StandardTrie("see a bear? sell stock! see a bull? buy stock! bid stock! bid stock! hear the bell? stop!")
    print(trie)

if __name__ == "__main__":
    main()



