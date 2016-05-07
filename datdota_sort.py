#!/usr/bin/env python3

from __future__ import division
from heroes import Hero
from heroes import print_hero_info

data = input('Enter the filename to analyze: ')

hero_list = []
with open(data) as f:
    for line in f.readlines():
        hero_name, _, __, won, lost = line.rsplit(None, 4)
        hero_list.append(Hero(hero_name, won, lost))
print_hero_info(hero_list)
