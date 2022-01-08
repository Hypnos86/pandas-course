# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


np.random.seed(0)

A = np.random.randint(0, 10, 10)

series = pd.Series(A, name = 'los')

# %%Examples 1
series.dtype
series.iloc[2]
series.iloc[-1]
series.index
series.name
series.shape

array_A = series.values

# %%Examples 2

N = np.random.rand(20)
M = np.random.rand(20)

series_N = pd.Series(N)
series_M = pd.Series(M)

series_N.abs()
series_N.add(series_M)
series_N.subtract(series_M)
series_N.divide(series_M)

series.drop_duplicates()
series[4] = np.nan
series.dropna()