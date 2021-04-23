# Attempt to answer the question of why strikeouts have increased
# # in the MLB. Look at homerun avg over time, look at launch angle
# over time, look at pitch velocity over time, look at exit velocity
# over time

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

import re

urlfile=""

mydata = pd.read_csv(urlfile)
