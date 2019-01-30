#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from math import ceil, sqrt


def eratosthenes(n):
    """
    Returns a list of all prime numbers up to a given limit using the sieve of
    Eratosthenes.
    """
    primes = 2 * [False] + (n - 1) * [True]
    for i in range(2, int(ceil(sqrt(n))) + 1):
        for j in range(i ** 2, n + 1, i):
            primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]


class TestEratosthenes(unittest.TestCase):
    def test_eratosthenes(self):
        self.assertListEqual(eratosthenes(0), [])
        self.assertListEqual(eratosthenes(10), [2, 3, 5, 7])
        self.assertListEqual(eratosthenes(19), [2, 3, 5, 7, 11, 13, 17, 19])


if __name__ == "__main__":
    unittest.main()
