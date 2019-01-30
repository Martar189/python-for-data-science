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


def longest_run_of_heads(n_flips, p_heads=0.5):
    current_run = 0
    longest_run = 0
    previous_flip_was_heads = None
    for i in range(n_flips):
        is_heads = random.random() < p_heads
        if is_heads and (previous_flip_was_heads is None or previous_flip_was_heads):
            current_run += 1
        else:
            longest_run = max(longest_run, current_run)
            current_run = 0
        previous_flip_was_heads = is_heads
    return longest_run


if __name__ == "__main__":
    random.seed(42)
    n_flips = ask_int("Number of flips? ")
    n_simulations = ask_int("Number of simulations? ")
    p_heads = 0.1
    while p_heads < 0.99:
        simulation_avg = (
            sum(longest_run_of_heads(n_flips, p_heads) for _ in range(n_simulations))
            / n_simulations
        )
        print(
            "P(heads) = {:3.1f} - Avg. longest run length = {:.2f}".format(
                p_heads, simulation_avg
            )
        )
        p_heads += 0.1
