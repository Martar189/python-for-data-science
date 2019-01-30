#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def first_negative_index(l):
    """
    Returns the index of the first negative element in a given list of numbers.
    """
    for i, x in enumerate(l):
        if x < 0:
            return i
    return None


class TestFirstNegativeIndex(unittest.TestCase):
    def test_first_negative_index(self):
        self.assertIsNone(first_negative_index([]))
        self.assertIsNone(first_negative_index([1, 3, 5, 7, 9]))
        self.assertEqual(first_negative_index([1, 3, -5, 7, -9]), 2)


if __name__ == "__main__":
    unittest.main()
