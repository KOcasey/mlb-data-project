import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

import re

urlfile="https://raw.githubusercontent.com/fivethirtyeight/data/master/mlb-quasi-win-shares/quasi_winshares.csv"

mydata = pd.read_csv(urlfile)

# avgWarPerSeason = mydata.groupby('year_ID', as_index=False)['WAR162'].agg(['mean', 'max'])
# avgWarPerSeason = pd.merge(avgWarPerSeason, mydata, left_on='max', right_on='WAR162')
# awps_x = avgWarPerSeason['year_ID']
# awps_y = avgWarPerSeason['mean']
# plt.scatter(awps_x, awps_y, s=10)

# # Add trendline
# z = np.polyfit(awps_x, awps_y, 1)
# p = np.poly1d(z)
# plt.plot(awps_x,p(awps_x),"r--")

# #add title
# plt.title('Average WAR of Each MLB Season Since 1901')

# #add x and y labels
# plt.xlabel('Year')
# plt.ylabel('WAR (wins above replacement)')

# plt.show()

war2019 = mydata.loc[mydata['year_ID'] == 2019]
war2019SS = war2019.loc[war2019['def_pos'].str.contains('.*SS.*')==True]
war20192B = war2019.loc[war2019['def_pos'].str.contains('.*2B.*')==True]

fig, (ax0, ax1) = plt.subplots(1, 2)
plt.sca(ax0)
plt.hist(war20192B['WAR162'], bins=20)
ax0.set(title='WAR for 2B 2019', xlabel='WAR(Wins Above Replacement)', ylabel='Count')

plt.sca(ax1)
plt.hist(war2019SS['WAR162'], bins=20)
ax1.set(title='WAR for SS 2019', xlabel='WAR(Wins Above Replacement)', ylabel='Count')
plt.show()

# # Title the figure
fig.suptitle('War Per Position 2019', fontsize=14, fontweight='bold');

#print(warPerPos2019.loc[warPerPos2019['def_pos']].head(10))

