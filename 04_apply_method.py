# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 21:57:25 2022

@author: kubia
"""

import pandas as pd
import numpy as np


np.random.seed(0)
# sigma = 10, mean = 5
s = pd.Series(10*np.random.rand(30)+5)

# %%

s.apply(abs)
s.apply(float.is_integer)
s.apply(int)

s.apply(lambda x: 100*x)

s_norm = s.apply(lambda x: x - np.mean(s))