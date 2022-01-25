#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:18:57 2022

@author: kamil
"""

import pandas as pd
import numpy as np

list_of_wig20 = ['ccc', 'amazon', 'CD projekt', 'JsW', 'Midas', 'energa', 'enea SA', 'alior', 'kghm']

wig20 = pd.Series(list_of_wig20, name='wig 20')

# %%

wig20_names = wig20.apply(lambda word: word.upper())

wig20_names.isin(['CCC'])

# %% stock len

stock_in_len = []

for company in wig20_names:
    if len(company) == 5:
        stock_in_len.append(company)
        print(company)

print(stock_in_len)