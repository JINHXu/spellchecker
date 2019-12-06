#!/usr/bin/env/python3

import unittest


from tries import StandardTrie

class TestStandardTrie(unittest.TestCase):

    def setUp(self):
        lexicon = ['bear', 'bell', 'bid', 'bull', 'buy', 'sell', 'stock', 'stop']
        self.test_trie = StandardTrie(lexicon)
    # an additional test for add() function? This seems pretty sufficient to me since every test for find() is based on the trie built through calling add().
    # testing add() by inspecting the children of each node?

    
    # multiple tests for find?
    def test_find_bear(self):
        self.assertEqual(self.test_trie.find('bear'), 'bear')

    def test_find_bell(self):
        self.assertEqual(self.test_trie.find('bell'), 'bell')
    
    def test_find_bid(self):
        self.assertEqual(self.test_trie.find('bid'), 'bid') 
    
    def test_find_bull(self):
        self.assertEqual(self.test_trie.find('bull'), 'bull')

    def test_find_buy(self):
        self.assertEqual(self.test_trie.find('buy'), 'buy')
    
    def test_find_sell(self):
        self.assertEqual(self.test_trie.find('sell'), 'sell')

    def test_find_stock(self):
        self.assertEqual(self.test_trie.find('stock'), 'stock')
    
    def test_find_stop(self):
        self.assertEqual(self.test_trie.find('stop'), 'stop')
    
    def test_incomplete_path(self):
        self.assertFalse(self.test_trie.find('bu'))

    def test_not_found(self):
        self.assertFalse(self.test_trie.find('blabla'))
    
    
    
    
    