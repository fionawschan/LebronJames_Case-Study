#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog
import pandas as pd 

gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)

df_bron_games_all = gamelog_bron_all.get_data_frames()[0]

df_bron_games_all.to_csv(path_or_buf="lebronAll.csv")


