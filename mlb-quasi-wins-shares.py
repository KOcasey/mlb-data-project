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
war20191B = war2019.loc[war2019['def_pos'].str.contains('.*1B.*')==True]
war20193B = war2019.loc[war2019['def_pos'].str.contains('.*3B.*')==True]
war2019LF = war2019.loc[war2019['def_pos'].str.contains('.*LF.*')==True]
war2019CF = war2019.loc[war2019['def_pos'].str.contains('.*CF.*')==True]
war2019RF = war2019.loc[war2019['def_pos'].str.contains('.*RF.*')==True]
war2019C = war2019.loc[(war2019['def_pos'].str.contains('.*C.*')==True) & (war2019['def_pos'].str.contains('.*CF.*')==False)]

#Set axis font size
plt.rcParams['axes.labelsize'] = 10

fig, axs = plt.subplots(2, 4, sharey=True)

fig.tight_layout(rect=[0, 0.03, 1, 0.9], pad=0.4, w_pad=0.5, h_pad=5.0)
# Title the figure
fig.suptitle('War Per Position 2019', fontsize=14, fontweight='bold')

plt.sca(axs[0,0])
plt.hist(war20192B['WAR162'], bins=20)
axs[0,0].set(title='WAR for 2B 2019', xlabel='WAR(Wins Above Replacement)', ylabel='Count')

plt.sca(axs[0,1])
plt.hist(war2019SS['WAR162'], bins=20)
axs[0,1].set(title='WAR for SS 2019', xlabel='WAR(Wins Above Replacement)', ylabel='')

plt.sca(axs[0,2])
plt.hist(war20191B['WAR162'], bins=20)
axs[0,2].set(title='WAR for 1B 2019', xlabel='WAR(Wins Above Replacement)', ylabel='')

plt.sca(axs[0,3])
plt.hist(war20193B['WAR162'], bins=20)
axs[0,3].set(title='WAR for 3B 2019', xlabel='WAR(Wins Above Replacement)', ylabel='')

plt.sca(axs[1,0])
plt.hist(war2019LF['WAR162'], bins=20)
axs[1,0].set(title='WAR for LF 2019', xlabel='WAR(Wins Above Replacement)', ylabel='Count')

plt.sca(axs[1,1])
plt.hist(war2019CF['WAR162'], bins=20)
axs[1,1].set(title='WAR for CF 2019', xlabel='WAR(Wins Above Replacement)', ylabel='')

plt.sca(axs[1,2])
plt.hist(war2019RF['WAR162'], bins=20)
axs[1,2].set(title='WAR for RF 2019', xlabel='WAR(Wins Above Replacement)', ylabel='')

plt.sca(axs[1,3])
plt.hist(war2019C['WAR162'], bins=20)
axs[1,3].set(title='WAR for C 2019', xlabel='WAR(Wins Above Replacement)', ylabel='')
plt.show()

#print(warPerPos2019.loc[warPerPos2019['def_pos']].head(10))

