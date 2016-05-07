from __future__ import division
from math import sqrt

confidence_percent = {
    95: 1.96,
    90: 1.645,
}

odd_names = {
    'Anti Mage': 'Anti-Mage',
    'Natures Prophet': "Nature's Prophet",
}
class Hero(object):
    def __init__(self, name, wins, losses):
        if name in odd_names.keys():
            name = odd_names[name]
        self.name = name.strip()
        self.wins = int(wins)
        self.losses = int(losses)
        self.confidence = round(self._confidence(), 4)

    def __str__(self):
        return '%s: %s (%s-%s)' % (self.name, self.confidence, self.wins, self.losses)

    def __eq__(self, other):
        return self.name == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def _confidence(self, z=95):  # Default z of 95%
        n = self.wins + self.losses
        z = confidence_percent[z]
        assert n != 0, 'Need usages to calculate lower bound of confidence interval'
        phat = float(self.wins) / n
        return (phat + z*z/(2*n) - z*sqrt((phat*(1-phat)+z*z/(4*n))/n)) / (1+z*z/n)

def print_hero_info(hero_stats):
    """ Takes a list of Hero objects and prints them nicely in ranked order.
        Also prints a list of unpicked heroes, based on the data set.
    """
    heroes = sorted(hero_stats, key=lambda x: (x.confidence, -x.losses), reverse=True)
    print('The "Best" Heroes from this tournament:\n')
    for index, hero in enumerate(heroes, start=1):
        print('%s. %s' % (index, hero))
    with open('heroes.txt') as file:
        all_heroes = set(hero.strip() for hero in file.readlines())
        unpicked_heroes = all_heroes - set(hero.name for hero in heroes)
        print('\nUnpicked Heroes (%s):\n\n- %s'
              % (len(unpicked_heroes), '\n- '.join(unpicked_heroes)))




