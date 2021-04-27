#Looks at the luckiest and unluckiest players to start the season
#to see if people will regress, improve, or keep pace

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

import re

urlfile2021 = "C:/Users/casey/OneDrive/Documents/GitHub_Projects/mlb-data-project/data/expected_stats_2021.csv"
urlfile2020 = "C:/Users/casey/OneDrive/Documents/GitHub_Projects/mlb-data-project/data/expected_stats_2020.csv"
urlfile2019 = "C:/Users/casey/OneDrive/Documents/GitHub_Projects/mlb-data-project/data/expected_stats_2019.csv"
urlfile2018 = "C:/Users/casey/OneDrive/Documents/GitHub_Projects/mlb-data-project/data/expected_stats_2018.csv"
urlfile2017 = "C:/Users/casey/OneDrive/Documents/GitHub_Projects/mlb-data-project/data/expected_stats_2017.csv"
urlfile2016 = "C:/Users/casey/OneDrive/Documents/GitHub_Projects/mlb-data-project/data/expected_stats_2016.csv"


data_2021 = pd.read_csv(urlfile2021)
data_2020 = pd.read_csv(urlfile2020)
data_2019 = pd.read_csv(urlfile2019)
data_2018 = pd.read_csv(urlfile2018)
data_2017 = pd.read_csv(urlfile2017)
data_2016 = pd.read_csv(urlfile2016)


dfs = [data_2020, data_2019, data_2018, data_2017, data_2016]
combined_df = pd.concat(dfs, join='inner')

five_yr_avg = combined_df.groupby('player_id').mean().reset_index()
five_yr_avg_ba = five_yr_avg[['player_id', 'ba']]
five_yr_avg_ba.columns = ['player_id', 'five_yr_ba']
print(five_yr_avg_ba[five_yr_avg_ba['player_id'] == 425877])

complete_df = pd.merge(data_2021, five_yr_avg_ba, how='outer', on='player_id')
complete_df = complete_df.assign(current_ba_diff=lambda df: df['ba'] - df['five_yr_ba'])
print(complete_df[complete_df['player_id'] == 425877])



