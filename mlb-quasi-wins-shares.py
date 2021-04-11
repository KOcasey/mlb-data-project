import numpy as np
import pandas as pd

from pandas import Series, DataFrame

urlfile="https://raw.githubusercontent.com/fivethirtyeight/data/master/mlb-quasi-win-shares/quasi_winshares.csv"

mydata = pd.read_csv(urlfile)
print(mydata.head(5))

