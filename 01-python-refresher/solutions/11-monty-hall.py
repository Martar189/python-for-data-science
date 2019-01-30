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


def simulate_monty_hall(rounds=10000):
    """
    Simulates several rounds of the Monty Hall game.
    Returns two Boolean values representing the outcome of the 'stay' and
    'switch' strategies.
    """
    wins_stay = 0
    wins_switch = 0
    for _ in range(rounds):
        car_position = random.randint(1, 3)
        switch_to = 3 if car_position != 2 else 2
        wins_stay += car_position == 1
        wins_switch += car_position == switch_to
    return wins_stay / rounds, wins_switch / rounds


if __name__ == "__main__":
    random.seed(42)
    rounds = ask_int("Number of rounds? ")
    p_win_stay, p_win_switch = simulate_monty_hall(rounds)
    print("P(win) if staying   = {:6.2f}%".format(p_win_stay * 100))
    print("P(win) if switching = {:6.2f}%".format(p_win_switch * 100))
