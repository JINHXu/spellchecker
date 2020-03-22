""" Spell checker.

    Author:      Jinghua Xu
    Description: A spell-checker class that stores a lexicon of words lexicon, in a Python set, and implements a method, check(word), which performs a spell check on the string word with respect to the words in lexicon.
    
    Honor Code:  I pledge that this program represents my own work.
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
        self._lexicon = set(lexicon)

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
        # word in lexicon
        if word in self._lexicon:
            spellings.append(word)
        # word not in lexicon
        else:
            for item in self._lexicon:
                dist = self.min_edit_distance(word, item)
                if dist == 1:
                    spellings.append(item)

        return spellings

    def min_edit_distance(self, source, target):
        """A helper function caluculating minimum edit distance between source and target.(a variant of Levinstein Distance: cost of deletion/substitution/insertion is one)

        Parameters
        ----------
        source : string
            The string to be spellchecked.
        target : string
            The string item in lexicon to be compared to source.

        Returns
        -------
        dist : int
            The minimum edit distance between source and target.
        """
        dist = 0
        n = len(source)
        m = len(target)
        # create a distance matrix distance[n+1, m+1], temporarily silled in with 'None'
        distance = []
        for i in range(n+1):
            distance.append([])
            for j in range(m+1):
                distance[i].append(0)

        # initialization: the zeroth row and col is the distance from the empty string
        distance[0][0] = 0

        # initiallize first col
        for i in range(1, n+1):
            distance[i][0] = distance[i-1][0] + 1
        # initialize first row
        for j in range(1, m+1):
            distance[0][j] = distance[0][j-1] + 1

        # recurrence relation
        for i in range(1, n+1):
            for j in range(1, m+1):
                # cell to the left in table plus one(cost)
                left = distance[i-1][j] + 1
                # cell above in table plus one(cost)
                up = distance[i][j-1] + 1
                # diagnoal value plus cost for substitution
                diagonal = distance[i-1][j-1]
                if source[i-1] != target[j-1]:
                    diagonal += 1
                    # fill in the cell
                distance[i][j] = min(left, up, diagonal)

        dist = distance[n][m]
        return dist
