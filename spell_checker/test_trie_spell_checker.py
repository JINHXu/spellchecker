#!/usr/bin/env/python3

import unittest

from spell_checker import TrieSpellChecker

class TestTrieSpellChecker(unittest.TestCase):

    def setUp(self):
        self.VOCAB_PATH = "spell_checker/data/SCOWL-wl/words.txt"
        self.TELEMARK_PATH = "spell_checker/data/0643/TELEMARKDAT.643"
        self.schecker = None

        with open(self.VOCAB_PATH, mode='r', encoding='utf8') as in_f:
            self.schecker = TrieSpellChecker([word.strip() for word in in_f.readlines()])
    
    def test_vocab(self):
        self.assertEqual(len(self.schecker.lexicon), 50166)

    def test_check(self):
        self.assertEqual(self.schecker.check("ansver")[0], "answer")

    def test_check_correct(self):
        self.assertEqual(self.schecker.check("answer")[0], "answer")

    def test_misspells(self):
        total = 0
        identif = 0
        with open(self.TELEMARK_PATH, mode='r', encoding='utf8') as in_f:
            for line in in_f.readlines():
                pieces = line.strip().split(" ")
                misspell = pieces[0]
                correct = pieces[1]
                if len(correct) > 3 and correct.isalnum() and misspell.isalnum() and correct.islower() and misspell.islower():
                    candidates = self.schecker.check(misspell)
                    if correct in candidates:
                        identif += 1
                        print("for misspelling ", misspell, " identified ", correct, " correctly. The list was ", candidates)
                    else:
                        print("no correct spelling identified for misspelling ", misspell, ". The correct spelling was ", correct, ".")

                    total += 1
        print("Identified %d correct spells out of %d." % (identif, total))
        self.assertEqual(identif, 673)
        