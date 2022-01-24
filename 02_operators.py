# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 18:51:06 2022

@author: kubia
"""

import pandas as pd
import numpy as np

# %%Example 1
np.random.seed(0) #ustawienie ziarna losowegp  - za kazdym uruchomieniem skrupyu te same obiekty
A = np.random.randint(1, 11, 10) #utworzenie tablicy numpy z przedzialu od 0 do 10 i losowanych jest 10


series = pd.Series(A, name='los') #twozymy tablice

# %% Example 2 - podstawowe atrybuty dla Series

series.dtype # sprawdza typ danych
series.iloc[3] #Wycinanie obiektu z listy
series.iloc[-3] #Wycinanie obiektu od konca listy
series.index 
series.name #sprawdzenie nazwy obiektu
series.shape #Sprawdzanie rozmiaru

array_A = series.values #konwersja obiektu syries na numy aray

# %% Example 3

N = np.random.rand(20)
M = np.random.rand(10)
series_N = pd.Series(N)
series_M = pd.Series(M)

# %% basic method

series_N.abs() #listuje wartosci bezwzględne
B = series_N.add(series_M) # dodaje listy do siebie po kazdym elemencie
C = series_N.sub(series_M) #odejmuje od siebie listy
D = series_N.divide(series_M) #dzieli obiekty z listy
E = series.drop_duplicates() #usuwa duplikaty
series[4] = np.nan #wyciecie z listy series 4tego elementu i przypisanie wartosci none
series.dropna() #usuwa puste wartosci z tablicy
series.idxmax() #wskazuje index na ktorym jest najwiekrza wartosc
series.idxmin() #wskazuje index na ktorym jest najwiekrza wartosc

F = series.count() #zlicza ilosc pozycji bez none
G = series_N.cumsum() #zlicza wartosci pokolei narastajaco
H = series_N.cummin() #wyszukuje wartosc najnizszą
I = series_N.cummax() #wyszukuje wartosc najwyzszą 
J = series_N.value_counts() #pokazuje ilosc wystepowania i sortuje
K =series_N.sum() # wartosc całej kolumny
L = series.std() #odchylenie standardowe
O = series.describe() #Opisuje liczbe wystąpień i inne wartosci - przydatne

# %% histogram

dist_data = pd.Series(np.random.rand(1000))
dist_data.hist(bins=50, color='pink') #tworzy histogram

# %% top n
top_3 = series_N.nlargest(3) #wskazuje n najlepsze elementy

# %% bottom n

bottom_4 = series_N.nsmallest(4) #wskazuje 4 najnizsze wartosci

q_1 = series_N.quantile(0.1)
q_2 = series_N.quantile(0.5)

P = series_N.round(2) # Zaokrąglenie

# %% 
shift_1 = series_N.shift(1)
shift_2_replace_0 = series.shift(2).fillna(0) #zastepuje puste miejsce zerem

# %% sort

series_sort = series_N.sort_values()
series_sort_asc = series_N.sort_values(ascending=False)



