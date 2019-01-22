#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def collatz():
    """
    Returns the Collatz sequence starting from a given number.
    """
    return


class TestCollatz(unittest.TestCase):
    def test_collatz(self):
        self.assertListEqual(collatz(42), [42, 21, 64, 32, 16, 8, 4, 2, 1])


if __name__ == "__main__":
    unittest.main()
