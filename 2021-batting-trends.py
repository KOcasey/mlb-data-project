#Looks at the luckiest and unluckiest players to start the season
#to see if people will regress, improve, or keep pace. Data is from 4/25/21

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
dfs = [data_2016, data_2017, data_2018, data_2019, data_2020]
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
# print(complete_df[complete_df['current_ba_diff'] >= 0.075])

#Buxton(621439), Trout(545361), Martinez(502110) for outperforming five_yr_ba by more than 0.075
#Sano(593934), McCutchen(457705), Freeman(518692) for undeperforming five_yr_ba by more than -0.075

#Set axis font size
plt.rcParams['axes.labelsize'] = 10

#Create plots with 2 rows and 4 columns
fig, axs = plt.subplots(1, 3, sharey=True)

#Format size and layout of subplots
fig.tight_layout(rect=[0, 0.03, 1, 0.9], pad=0.4, w_pad=0.5, h_pad=5.0)

#Title the Batting Trends figure
fig.suptitle('Batting Trends', fontsize=14, fontweight='bold')

#Set x axes for all figures
x = [2016, 2017, 2018, 2019, 2020, 2021]

#Buxton Figure
#Gets Buxton's 2021 batting average
buxton_2021_avg = data_2021[data_2021['player_id'] == 621439]
buxton_2021_avg = buxton_2021_avg['ba']

#Gets the rest of the years batting averages
#However we are missing 2018 because buxton got hurt and didn't have enough plate appearances to qualify
buxton_df = combined_df[combined_df['player_id'] == 621439]
buxton_y = buxton_df['ba'].to_numpy()
buxton_y = np.append(buxton_y, buxton_2021_avg)

#Insert buxton's 2018 average, it could slightly sway the data as it's not indicative of a full season
buxton_y = np.insert(buxton_y, 2, 0.156)

plt.sca(axs[0])
plt.plot(x, buxton_y)
axs[0].set(title='Byron Buxton', xlabel='Year', ylabel='Batting Average')
axs[0].axhline(y=buxton_y[0:4].mean(), color='r', linestyle='dashed', linewidth=2)


#Trout Figure
#Gets Trout's 2021 batting average
trout_2021_avg = data_2021[data_2021['player_id'] == 545361]
trout_2021_avg = trout_2021_avg['ba']

#Gets the rest of the years batting averages 2016-2020
trout_df = combined_df[combined_df['player_id'] == 545361]
trout_y = trout_df['ba'].to_numpy()
trout_y = np.append(trout_y, trout_2021_avg)

plt.sca(axs[1])
plt.plot(x, trout_y)
axs[1].set(title='Mike Trout', xlabel='Year', ylabel='Batting Average')
axs[1].axhline(y=trout_y[0:4].mean(), color='r', linestyle='dashed', linewidth=2)


#J.D. Martinez Figure
#Gets Martinez's 2021 batting average
martinez_2021_avg = data_2021[data_2021['player_id'] == 502110]
martinez_2021_avg = martinez_2021_avg['ba']

#Gets the rest of the years batting averages 2016-2020
martinez_df = combined_df[combined_df['player_id'] == 502110]
martinez_y = martinez_df['ba'].to_numpy()
martinez_y = np.append(martinez_y, martinez_2021_avg)

plt.sca(axs[2])
plt.plot(x, martinez_y)
axs[2].set(title='J.D. Martinez', xlabel='Year', ylabel='Batting Average')
axs[2].axhline(y=martinez_y[0:4].mean(), color='r', linestyle='dashed', linewidth=2)

#Show the plots
plt.show()

