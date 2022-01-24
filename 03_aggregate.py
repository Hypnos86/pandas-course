# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 21:29:42 2022

@author: kubia
"""

import pandas as pd
import numpy as np

# %% generatingsome data

np.random.seed(0)

s = pd.Series(np.random.rand(20))

# %% aggregate

minimum = s.aggregate(min)
maximum = s.aggregate(max)

suma = s.aggregate(sum)
mean = s.aggregate(np.mean) #liczy rednią
std = s.aggregate(np.std)

# %% agregacje wielopoziomowe

stats = s.aggregate(['min', 'max', 'sum'])
stats_np = s.aggregate([np.mean, np.std, np.median])
