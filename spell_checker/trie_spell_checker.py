""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 2
   
    Problem 3: Spell checker using a trie.

    Course:      Data Structures and Algorithms for CL III - WS1920
    Assignment:  lab 2, exercise 3
    Author:      Jinghua Xu
    Description: A spell checker implemented with trie, i.e. lexicon will be stored in a trie instead of a set.
    Honor Code:  I pledge that this program represents my own work.
"""

from tries.standard_trie import StandardTrie


class TrieSpellChecker:

    def __init__(self, lexicon):
        self._lexicon = StandardTrie(lexicon)

    @property
    def lexicon(self):
        return self._lexicon

    # starting from root node and first row in table
    def check(self, word):
        """ Checks if a given string word is correctly spelled (i.e. if it is in the trie spell checker's lexicon). If the string is not in the lexicon, then it returns a list of potentially correct spellings of the word from the trie spell checker's lexicon.(with a trie)

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

        # word in lexicon
        if self._lexicon.find(word):
            spellings.append(word)

        # word not in lexicon
        else:

            root_node = self._lexicon.root

            # build the first row
            current_row = range(len(word) + 1)

            # recursively checking children
            for child in root_node.children:
                self._recursiveCheck(child, child.key, word,
                                    current_row, spellings)

        return spellings

    def _recursiveCheck(self, node, char, word, previous_row, spellings):
        """ A helper function: the recursive call of check() function

        Parameters
        ----------
        self : TrieSpellChecker
            self to call this method
        node : Node
            Current node

        char : String
            Key of current node

        previous_row : list
            List stores previous row of the table(minimum edit distance matrix)

        spellings : list
            A list of correct/possible spellings of word, will be updated here

        Returns:
            None

        """

        # initial set up building current row
        num_cols = len(word) + 1
        current_row = [previous_row[0] + 1]

        # building current row with the information from previous row
        for col in range(1, num_cols):

            left = current_row[col - 1] + 1
            up = previous_row[col] + 1
            diagonal = previous_row[col - 1]

            if word[col - 1] != char:
                diagonal += 1

            current_row.append(min(left, up, diagonal))

        # distance does not reach threshold(1) and have reached leaf node: an acceptable spelling in trie => add the word in trie to spellings list
        if current_row[-1] <= 1 and node.value != None:
            spellings.append(node.value)

        # distance does not reach threshold(1) and have not reached leaf node: continue recursive search
        if min(current_row) <= 1:
            for child in node.children:
                self._recursiveCheck(child, child.key, word,
                                    current_row, spellings)
