import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

urlfile="https://raw.githubusercontent.com/fivethirtyeight/data/master/mlb-quasi-win-shares/quasi_winshares.csv"

mydata = pd.read_csv(urlfile)

avgWarPerSeason = mydata.groupby('year_ID', as_index=False)['WAR162'].agg(['mean', 'max'])
avgWarPerSeason = pd.merge(avgWarPerSeason, mydata, left_on='max', right_on='WAR162')
awps_x = avgWarPerSeason['year_ID']
awps_y = avgWarPerSeason['mean']
plt.scatter(awps_x, awps_y, s=10)

# Add trendline
z = np.polyfit(awps_x, awps_y, 1)
p = np.poly1d(z)
plt.plot(awps_x,p(awps_x),"r--")

#add title
plt.title('Average WAR of Each MLB Season Since 1901')

#add x and y labels
plt.xlabel('Year')
plt.ylabel('WAR (wins above replacement)')

plt.show()
print(mydata[['def_pos', 'pct_PT', 'WAR162']].head(5))

