#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def ask_int(prompt=None):
    answer = None
    while not answer:
        try:
            answer = int(input(prompt))
        except ValueError:
            pass
    return answer


def flip_until_equal(p_heads=0.5):
    n_heads = 0
    n_tails = 0
    while True:
        is_heads = random.random() < p_heads
        n_heads += is_heads
        n_tails += not is_heads
        if n_heads == n_tails:
            return n_heads * 2


if __name__ == "__main__":
    random.seed(42)
    n_simulations = ask_int("Number of simulations? ")
    p_heads = 0.1
    while p_heads < 0.99:
        simulation_avg = (
            sum(flip_until_equal() for _ in range(n_simulations)) / n_simulations
        )
        print(
            "P(heads) = {:3.1f} - Avg. number of flips = {:.2f}".format(
                p_heads, simulation_avg
            )
        )
        p_heads += 0.1
