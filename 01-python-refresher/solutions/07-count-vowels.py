#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def count_vowels(string):
    """
    Returns the number of vowels in a given string.
    """
    count = 0
    for character in string.lower():
        if character in "aeiou":
            count += 1
    return count


class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        pangram = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(count_vowels(pangram), 11)


if __name__ == "__main__":
    unittest.main()
