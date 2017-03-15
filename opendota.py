#!/usr/bin/env python3

from __future__ import division
from heroes import Hero
from heroes import print_hero_info
import urllib
import requests

sql = urllib.quote_plus('''
  SELECT *
  FROM heroes 
  LEFT JOIN 
  (SELECT hero_id as id, count(*) matches, sum(case when (player_matches.player_slot < 128) = radiant_win then 1 else 0 end) wins
  FROM player_matches 
  JOIN matches USING(match_id) 
  WHERE leagueid = 5157 
  GROUP BY hero_id)
  herodata USING(id)
  ORDER BY matches desc''')
url = 'http://api.opendota.com/api/explorer?sql=' + sql;
data = requests.get(url).json()
hero_list = []
for item in data['rows']:
  name = item['localized_name']
  matches = int(item['matches'] or 0)
  wins = int(item['wins'] or 0)
  losses = matches - wins
  if matches > 0:
    hero_list.append(Hero(name, wins, losses))
print_hero_info(hero_list)