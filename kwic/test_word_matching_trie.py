#!/usr/bin/env/python3

import unittest
import string

from kwic.word_matching_trie import WordMatchingTrie


class TestWordMatchingTrie(unittest.TestCase):

    def setUp(self):
        original_text = "see a bear? sell stock! see a bull? buy stock! bid stock! bid stock! hear the bell? stop!"

        self.wm_trie = WordMatchingTrie(original_text)

    def test_find_see(self):
        self.assertEqual(self.wm_trie.find('see'), [0, 24])

    def test_find_bell(self):
        self.assertEqual(self.wm_trie.find('bell'), [78])

    def test_find_stock(self):
        self.assertEqual(self.wm_trie.find('stock'), [17, 40, 51, 62])

    def test_incomplete_path(self):
        self.assertFalse(self.wm_trie.find("bea"))

    def test_not_found(self):
        self.assertFalse(self.wm_trie.find("babel"))
