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

#Create a list of my dataframes from 2016 to 2020 and combine them together
dfs = [data_2020, data_2019, data_2018, data_2017, data_2016]
combined_df = pd.concat(dfs, join='inner')

#Group the combined dfs to get the mean values for each player from 2016 to 2020
five_yr_avg = combined_df.groupby('player_id').mean().reset_index()
five_yr_avg_ba = five_yr_avg[['player_id', 'ba']]

#Rename grouped 'ba' column to 'five_yr_ba'
five_yr_avg_ba.columns = ['player_id', 'five_yr_ba']
print(five_yr_avg_ba[five_yr_avg_ba['player_id'] == 425877])

#Merge the 2021 dataframe and the five_yr_avg dataframe to add the five_yr_ba column to the 2021 data
complete_df = pd.merge(data_2021, five_yr_avg_ba, how='outer', on='player_id')

#Create the difference between current batting avg and mean five_yr_batting_avg column
complete_df = complete_df.assign(current_ba_diff=lambda df: df['ba'] - df['five_yr_ba'])
complete_df = complete_df[['last_name', 'player_id', 'pa', 'ba','five_yr_ba', 'current_ba_diff']]
print(complete_df[complete_df['current_ba_diff'] >= 0.075])



