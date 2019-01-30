#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def first_negative(l):
    """
    Returns the first negative element in a given list of numbers.
    """
    for x in l:
        if x < 0:
            return x
    return None


class TestFirstNegative(unittest.TestCase):
    def test_first_negative(self):
        self.assertIsNone(first_negative([]))
        self.assertIsNone(first_negative([1, 3, 5, 7, 9]))
        self.assertEqual(first_negative([1, 3, -5, 7, -9]), -5)


if __name__ == "__main__":
    unittest.main()
