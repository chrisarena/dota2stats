#!/usr/bin/env python3

from __future__ import division
from heroes import Hero
from heroes import print_hero_info

data = input('Enter the filename to analyze: ')

print('\n\n')
with open(data) as file:
    hero_list = []
    while True:
        try:
            name, _, matches, winrate = [next(file) for _ in range(4)]
            matches = int(matches)
            winrate = float(winrate.strip().strip('%')) / 100
            wins = int(round(winrate * matches))
            losses = matches - wins
            hero_list.append(Hero(name, wins, losses))
        except StopIteration:
            break
    print_hero_info(hero_list)
