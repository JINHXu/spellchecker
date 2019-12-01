#!/usr/bin/env/python3

import unittest

from tries.standard_trie import StandardTrie

class TestStandardTrie(unittest.TestCase):

    def setup(self):
        lexicon = {'bear', 'bell', 'bid', 'bull', 'buy', 'sell', 'stock', 'stop'}
        self.test_trie = StandardTrie(lexicon)


    def test_add(self):
        expected_trie = 'None:None\n\t\'b\':None\n\t*2\'u\':None\n\t*3\'l\':None\n\t*4\'l\':\'bull\'\n\t*3\'y\':\'buy\'\n\t\t\'i\':None\n\t*3\'d\':\'bid\'\n\t*2\'e\':None\n\t*3\'l\':None\n\t*4\'l\':\'bell\'\n\t*3\'a\':None\n\t*4\'r\':\'bear\'\n\t\'s\':None\n\t*2\'t\':None\n\t*3\'o\':None\n\t*4\'p\':\'stop\'\n\t*4\'c\':None\n\t*5\'k\':\'stock\'\n\t*2\'e\':None\n\t*3\'l\':None\n\t*4\'l\':\'sell\''
        self.assertEqual(str(self.test_trie), expected_trie)

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
    
    
    
    
    