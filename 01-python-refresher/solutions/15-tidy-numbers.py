#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_tidy(number):
    digits = [int(x) for x in str(number)]
    return digits == sorted(digits)


def last_tidy_number(n):
    while not is_tidy(n):
        n -= 1
    return n


if __name__ == "__main__":
    n = None
    while not n:
        try:
            n = int(input("n = "))
        except ValueError:
            pass
    print("Last tidy number = {}".format(last_tidy_number(n)))
