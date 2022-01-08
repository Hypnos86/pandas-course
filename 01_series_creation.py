# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %%Examples 1
s = pd.Series(4)

# %% Examples 2
s_def = pd.Series(data=[21, 45, 23], index=['kamil', 'darek', 'piotr'], name='wiek')
                  
# %% Examples 3
A = np.random.rand(20)
s = pd.Series(A)

# %%Examples 4
stocks = {'Apple':'USA', 'CD Project':'Poland', 'JSW':'Poland', 'Prada':'GB'}
series = pd.Series(stocks, name='kraj')

# %%Example 5
stock_price = {'Apple':234, 'CD Project':180, 'Amazon':638}
stock_price_series = pd.Series(stock_price, name = 'price')

stock_price_array = stock_price_series.values

apple_price = stock_price_series['Apple']

'Apple' in stock_price_series

# %%Examples 6 
np.random.seed(0)

A = np.random.rand(20)
a = pd.Series(A)