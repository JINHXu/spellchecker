""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 2
   
    Problem 2: Standard Trie

    Course:      Data Structures and Algorithms for CL III - WS1920
    Assignment:  lab 2, exercise 2
    Author:      Jinghua Xu
    Description: an implementation of a standard trie class
 
    Honor Code:  I pledge that this program represents my own work.
"""

class StandardTrie:
    """Representation of a standard trie where words are stored as node values."""

    def __init__(self, strings):
        """ Constructor for StandardTrie. Builds the trie based on the supplied string collection.
        
        Parameters
        ----------
        strings : iterable
            An iterable over the strings to be used for constructing the trie.
        """
        self._root = self.Node()

        for s in strings:
            self.add(s, s)

    @property
    def root(self):
        return self._root

    def add(self, string, value):
        """ Adds a new (string, value) pair to the trie. The value should be 
        added to the node having the last letter of the string as a key.
        
        Parameters
        __________
        string : string
            The string to add to the trie.
        value : object
            The value associated to the string.
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
        node._value = value

    def find(self, pattern):
        """ Finds the value associated with the pattern.
        
        Parameters
        ----------
        pattern : string
            The string pattern to search in the trie.
        
        Returns
        -------
        value : object
            The value associated with the pattern, if the pattern is part of the
         trie. Returns False is the pattern is not in the trie.   
        """
        # current node
        node = self._root
        
        #search in an empty trie?
        if not node._children:
            print('search in an empty trie')
            return False

        for char in pattern:
            char_not_found = True
            for child in node._children:
                if child.key == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False

        if not node._value:
            return False
        else:
            return node._value


    def node_size(self):
        return self.root.node_size()

    def __len__(self):
        return self.root.word_size()

    def __str__(self):
        return f"{self.root}\nThe trie has {len(self)} words in {self.node_size()} nodes."

    class Node:
        """ Class for representing a node in a standard trie."""
        __slots__ = '_children', '_key', '_value'

        def __init__(self):
            """ Do not call this constructor directly."""
            self._children = {}
            self._key = None
            self._value = None

        @property
        def children(self):
            return self._children

        @property
        def key(self):
            return self._key

        @key.setter
        def key(self, new_key):
            self._key = new_key 

        @property
        def value(self):
            return self._value

        def word_size(self):
            """ Computes how many words are in the subtree rooted at this node."""
            size = 1 if self.value else 0
            for child in self.children.values():
                size += child.word_size()
            return size

        def node_size(self):
            """ Computes how many nodes are in the subtree rooted at this node."""
            size = 1
            for child in self.children.values():

                size += child.node_size()
            return size

        def _node_repr(self, level=0):
            """ Returns a string representation of the subtree rooted at this node, indented according to its level."""
            rep = "{}{}:{}\n".format("\t" * level, repr(self.key), repr(self.value))
            for v in self.children.values():
                rep += v._node_repr(level + 1)
            return rep     

        def __str__(self):
            return self._node_repr()

def main():
    trie = StandardTrie(['bull', 'buy', 'bid', 'bell', 'bear', 'stop', 'stock', 'sell'])
    print(trie)
    print(trie.find('buy'))

if __name__ == "__main__":
    main()
