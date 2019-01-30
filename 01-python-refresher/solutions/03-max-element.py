#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def max_element(l):
    """
    Returns the maximum element of a given list of numbers.
    """
    max_ = None
    for x in l:
        if max_ is None or x > max_:
            max_ = x
    return max_


class TestMaxElement(unittest.TestCase):
    def test_max_element(self):
        self.assertIsNone(max_element([]))
        self.assertEqual(max_element([1, 3, -5, 7, -9]), 7)


if __name__ == "__main__":
    unittest.main()
