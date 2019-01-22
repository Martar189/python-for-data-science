#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def count_vowels():
    """
    Returns the number of vowels in a given string.
    """
    return


class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        pangram = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(count_vowels(pangram), 11)


if __name__ == "__main__":
    unittest.main()
