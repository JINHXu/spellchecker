#!/usr/bin/env/python3

import unittest

from spell_checker import SpellChecker

class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.LEXICON_PATH = "spell_checker/data/SCOWL-wl/words.txt"
        self.TELEMARK_PATH = "spell_checker/data/0643/TELEMARKDAT_sample.643"
        self.schecker = None
        with open(self.LEXICON_PATH, mode='r', encoding='utf8') as in_f:
            self.schecker = SpellChecker(word.strip() for word in in_f)

    def test_vocab(self):
        self.assertEqual(len(self.schecker.lexicon), 50166)

    def test_check(self):
        self.assertEqual(self.schecker.check("ansver")[0], "answer")

    def test_misspells(self):
        total = 0
        identif = 0
        with open(self.TELEMARK_PATH, mode='r', encoding='utf8') as in_f:
            for line in in_f:
                misspell, correct = line.strip().split(" ")[:2]
                if len(correct) > 3:
                    candidates = self.schecker.check(misspell)
                    total += 1
                    if correct in candidates:
                        identif += 1
                        print(total, ": for misspelling ", misspell, " identified ", correct, " correctly. The list was ", candidates)
                    else:
                        print(total, ": no correct spelling identified for misspelling ", misspell, ". The correct spelling was ", correct, ".")


        print("Identified %d correct spells out of %d." % (identif, total))
        self.assertEqual(identif, 31)
        