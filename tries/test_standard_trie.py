#!/usr/bin/env/python3

""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 2
   
    Problem 2: Standard Trie unit test

    Course:      Data Structures and Algorithms for CL III - WS1920
    Assignment:  lab 2, exercise 2
    Author:      Jinghua Xu
    Description: unit test for StandardTrie
 
    Honor Code:  I pledge that this program represents my own work.
"""

import unittest

from tries import StandardTrie


class TestStandardTrie(unittest.TestCase):

    def setUp(self):
        lexicon = ['bear', 'bell', 'bid', 'bull',
                   'buy', 'sell', 'stock', 'stop']
        self.test_trie = StandardTrie(lexicon)

    def test_add(self):
        words = set(["bell"])
        trie = StandardTrie(words)

        self.assertEqual(len(trie), 1)
        self.assertEqual(trie.node_size(), 5)

    def test_add_2(self):
        words = set(["stop", "stock"])
        trie = StandardTrie(words)

        self.assertEqual(len(trie), 2)
        self.assertEqual(trie.node_size(), 7)

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
