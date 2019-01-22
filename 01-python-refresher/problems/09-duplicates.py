#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def has_duplicates():
    """
    Returns whether a given list contains duplicate elements.
    """
    return


class TestHasDuplicates(unittest.TestCase):
    def test_has_duplicates(self):
        self.assertTrue(has_duplicates([0, 0]))
        self.assertFalse(has_duplicates("uncopyrightable"))


if __name__ == "__main__":
    unittest.main()
