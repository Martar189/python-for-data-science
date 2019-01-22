#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def max_element():
    """
    Returns the maximum element of a given list of numbers.
    """
    return


class TestMaxElement(unittest.TestCase):
    def test_max_element(self):
        self.assertIsNone(max_element([]))
        self.assertEqual(max_element([1, 3, -5, 7, -9]), 7)


if __name__ == "__main__":
    unittest.main()
