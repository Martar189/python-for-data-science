#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def c_to_f(temperature):
    """
    Converts a temperature in Celsius to Fahrenheit.
    """
    return temperature * 9 / 5 + 32


def f_to_c(temperature):
    """
    Converts a temperature in Fahrenheit to Celsius.
    """
    return (temperature - 32) * 5 / 9


class TestTemperatureConversion(unittest.TestCase):
    def test_c_to_f(self):
        self.assertAlmostEqual(c_to_f(0), 32)
        self.assertAlmostEqual(c_to_f(100), 212)

    def test_f_to_c(self):
        self.assertEqual(f_to_c(32), 0)
        self.assertEqual(f_to_c(212), 100)


if __name__ == "__main__":
    unittest.main()
