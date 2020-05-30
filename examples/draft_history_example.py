#!/usr/bin/env python3

from nba_api.stats.endpoints import drafthistory

dh = drafthistory.DraftHistory()

print(len(dh.data_sets))
for i in dh.data_sets:
    print(i.get_json())


