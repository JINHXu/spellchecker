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
    
    def check(self, word):
        
        spellings = []

        if self.lexicon.find(word):
            spellings.append(word)

        else:
            # go through each paths(from root node to leaf nodes) in the trie
            # a BFS search
            node = self.lexicon.root
            for child in node.children:
                if 
                
        return spellings
        
    # the variant of min_edit_distance: takes a row and returns a row
    def min_edit_distance(self, source, target):

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
            distance[0][j] = distance[0][j-1] +1

        #recurrence relation
        for i in range(1,n+1):
            for j in range(1, m+1):
                # cell to the left in table
                left = distance[i-1][j] + 1
                # cell above in table
                up = distance[i][j-1] + 1
                diagonal = distance[i-1][j-1]
                if source[i-1] != target[j-1]:
                    diagonal += 1
                distance[i][j] = min(left, up, diagonal)

        return min(distance[n])


#min_edit_diatnce() works
def main():
        tmp = SpellChecker({1})
        print(tmp.min_edit_distance('b','bell'))

if __name__ == "__main__":
        main()
    