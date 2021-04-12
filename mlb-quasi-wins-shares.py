import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

urlfile="https://raw.githubusercontent.com/fivethirtyeight/data/master/mlb-quasi-win-shares/quasi_winshares.csv"

mydata = pd.read_csv(urlfile)

bestWarPerSeason = mydata.groupby('year_ID', as_index=False)['WAR162'].max()
bestWarPerSeason = pd.merge(bestWarPerSeason, mydata, on='WAR162')
bwps_x = bestWarPerSeason['year_ID_x']
bwps_y = bestWarPerSeason['WAR162']
plt.scatter(bwps_x, bwps_y, s=10)

# Add trendline
z = np.polyfit(bwps_x, bwps_y, 1)
p = np.poly1d(z)
plt.plot(bwps_x,p(bwps_x),"r--")

#add title
plt.title('Highest WAR of Each MLB Season Since 1901')

#add x and y labels
plt.xlabel('Year')
plt.ylabel('WAR (wins above replacement)')

plt.show()
# print(bestWarPerSeason.columns)

