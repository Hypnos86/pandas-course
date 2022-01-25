#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:41:43 2022

@author: kamil
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # biblioteka do wizualizacji w pythonie

patch = '/Users/kamil/Desktop/Projekty/pandas-course/data/amzn_us_d.csv'

amz = pd.read_csv(patch, index_col=0)

close = amz['Zamkniecie']

close = close['2020-01-01':]

# %% ploting he results

close.plot(title='wykres nowotan Amazon')
plt.savefig('./charts/close.png', format='png')