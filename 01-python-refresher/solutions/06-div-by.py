#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def div_by(upper_limit, divisors):
    """
    Returns a list of the numbers between 1 and a given upper limit that are
    divisible by at least one element of a given list of divisors.
    """
    result = []
    for i in range(1, upper_limit + 1):
        for divisor in divisors:
            if i % divisor == 0:
                result.append(i)
                break
    return result


class TestDivBy(unittest.TestCase):
    def test_div_by(self):
        self.assertListEqual(div_by(100, [50]), [50, 100])
        self.assertListEqual(div_by(100, [50, 75]), [50, 75, 100])


if __name__ == "__main__":
    unittest.main()
