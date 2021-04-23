#Looks at the luckiest and unluckiest players to start the season
#to see if people will regress, improve, or keep pace

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

import re

urlfile=""

mydata = pd.read_csv(urlfile)