#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:50:25 2020

@author: fifi
"""

import pandas as pd
from nba_api.stats.static import players
player_dict = players.get_players()

bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog
import pandas as pd 

gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season = '2018')
df_bron_games_2018 = gamelog_bron.get_data_frames()[0]

gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)
df_bron_games_all = gamelog_bron_all.get_data_frames()[0]

df = df_bron_games_all
df.to_excel("lebronAll.xlsx")

