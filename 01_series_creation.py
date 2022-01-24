# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 09:46:37 2022

@author: kubia
"""

import pandas as pd
import numpy as np

# %%Example 1

s = pd.Series(4)

# %%Example 2
s_def = pd.Series(data=[21,15,54], index=['Kamil','Kasia', 'Gosia'], name='wiek')

# %%Example 3
A = np.random.rand(10)
s = pd.Series(A)

# %%Example 4
stocks = {'Apple':'USA', 'CD Projekt':'Poland', 'Amazon':'USA'}
series = pd.Series(stocks)
