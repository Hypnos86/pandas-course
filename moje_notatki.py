#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:51:31 2022

@author: kamil
"""

import pandas as pd
import numbers as np

# %% importowanie pliku

units_list = pd.read_csv('./data/units.csv', sep='|')

# %% wycinanie kolumny z miastem
miasta = units_list['miasto']

# %% jednostki ID - stworzenie obrazka

id_jednostki = units_list['nr_jednostki']
id_jednostki.plot(title='id jednostek')