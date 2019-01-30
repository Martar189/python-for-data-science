#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def has_duplicates(l):
    """
    Returns whether a given list contains duplicate elements.
    """
    seen = set()
    for x in l:
        if x in seen:
            return True
        seen.add(x)
    return False


class TestHasDuplicates(unittest.TestCase):
    def test_has_duplicates(self):
        self.assertTrue(has_duplicates([0, 0]))
        self.assertFalse(has_duplicates("uncopyrightable"))


if __name__ == "__main__":
    unittest.main()
