#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def eratosthenes():
    """
    Returns a list of all prime numbers up to a given limit using the sieve of
    Eratosthenes.
    """
    return


class TestEratosthenes(unittest.TestCase):
    def test_eratosthenes(self):
        self.assertListEqual(eratosthenes(0), [])
        self.assertListEqual(eratosthenes(10), [2, 3, 5, 7])
        self.assertListEqual(eratosthenes(19), [2, 3, 5, 7, 11, 13, 17, 19])


if __name__ == "__main__":
    unittest.main()
