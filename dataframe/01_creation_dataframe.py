#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:02:22 2022

@author: kamil
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(data=[1,2,3,4,5,3,3,2])

df = pd.DataFrame(data=[[1,2,3], [3,4,5]], index=['first', 'second'], columns=['pierwsza', 'droga', 'trzecia'])