import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

urlfile="https://raw.githubusercontent.com/fivethirtyeight/data/master/mlb-quasi-win-shares/quasi_winshares.csv"

mydata = pd.read_csv(urlfile)

# bestWarPerSeason = mydata[['name_common','team_ID', 'year_ID', 'WAR162']]
# bestWarPerSeason = bestWarPerSeason.groupby('year_ID')
# bestWarPerSeason = bestWarPerSeason.max('WAR162')
bestWarPerSeason = mydata.groupby('year_ID', as_index=False)['WAR162'].max()
bestWarPerSeason = pd.merge(bestWarPerSeason, mydata, on='WAR162')
print(bestWarPerSeason.tail(5))

