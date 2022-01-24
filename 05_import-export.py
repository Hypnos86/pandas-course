#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 21:00:27 2022

@author: kamil
"""

import pandas as pd
import numpy as np


df = pd.read_csv('./data/cdr_d.csv', index_col = 0) # eksportuje dane

close_price  =df['Zamkniecie'] # wycina konkretna kolumne


# %% export to csv
close_price.to_csv('./data/csv_zamkniecie.csv', header=['close'])

# %% export to json
 close_price.to_json('./data/zamkniecie.json')
 
# %% export to python dict
 
 cpd = close_price.to_dict()
 
 # %% Wycinanie ze schowka do Data frame
 clipboard =_df = pd.read_clipboard()