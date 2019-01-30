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


def has_duplicates(l):
    seen = set()
    for x in l:
        if x in seen:
            return True
        seen.add(x)
    return False


def roll_has_duplicates(n_dice):
    return has_duplicates(random.randint(1, 6) for _ in range(n_dice))


if __name__ == "__main__":
    random.seed(42)
    n_simulations = ask_int("Number of simulations? ")

    for n_dice in range(2, 11):
        simulation_prop = (
            sum(roll_has_duplicates(n_dice) for _ in range(n_simulations))
            / n_simulations
        )
        print(
            "Dice = {:2d} - Rolls with duplicates = {:6.2f}%".format(
                n_dice, simulation_prop * 100
            )
        )
