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


data_2021 = pd.read_csv(urlfile2021)
data_2020 = pd.read_csv(urlfile2020)
data_2019 = pd.read_csv(urlfile2019)
data_2018 = pd.read_csv(urlfile2018)
data_2017 = pd.read_csv(urlfile2017)