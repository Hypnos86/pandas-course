#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 19:00:16 2022

@author: kamil
"""

import pandas as pd
import numpy as np

# %% import pliu
df = pd.read_csv('../data/aapl_us_d.csv', index_col=0)
df.columns=['Open', 'High', 'low', 'close', 'volume']

# %%
print(df.columns)

# %% wycinanie - trzy sposobu

open_price = df['Open']
open_price = df.iloc[:, 0]
open_proce = df.Open

high_proce = df['close']

# %%

last_column = df.iloc[:, -1]
# %%

two = df[['Open', 'close']]
second = df.iloc[: , [0,3]]

# %%
from_opne_to_close = df.iloc[:,0:4]

# %% wycinanie tylko pierwszego wiersza
x = df.iloc[0:5,:2]

# %% nowa kolumna - średnia

df['average'] = df['Open'] + df['close'] / 2.

# %%  obliczanie nowej kolumny z przesunieciem
k = df['Daily_change'] = df['close'] / df['close'].shift(1) - 1

y = df.shift(1)

# %% średnia

df = df.assign(avg=(df['Open'] +df['close'] / 2.))

# %%
max_daily_change = df['Daily_change'].aggregate(max)
min_daily_change = df['Daily_change'].aggregate(min)

df['Daily_change'].hist(bins=100) # histogram

# %%
df['Flag'] = df['Daily_change']>0

df['Flag'].aggregate(sum)

days_wyth_positive_return = df['Flag'].aggregate(sum) / df['Flag'].aggregate('count')

days = df['Open'].plot()




