# -*- coding: utf-8 -*-
"""
Created on Fri May 13 08:26:58 2016

@author: ouj070
"""

import re
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import xticks

# Creating Month
movie_final['month'] = pd.DataFrame([pd.to_datetime(date) for date in movie_final['release_date']])

movie_final['month'] = movie_final['month'].dt.month

a = movie_final['month'].dropna()

plt.hist(a)

# Create Seasons
movie_final['Season'] = 0
idx = movie_final['month'].isin([2,3,4])
movie_final['Season'][idx] = 1
idx = movie_final['month'].isin([5,6,7])
movie_final['Season'][idx] = 2
idx = movie_final['month'].isin([8,9,10])
movie_final['Season'][idx] = 3
idx = movie_final['month'].isin([11,12,1])
movie_final['Season'][idx] = 4

plt.hist(movie_final['Season'], bins=range(5))
plt.xticks(range(4))
plt.xlim([0, 4])

#Create Metascore categories
movie_final['Scoregroup'] = 0
idx = movie_final['metascore'].isin(range(20,40))
movie_final['Scoregroup'][idx] = 1
idx = movie_final['metascore'].isin(range(40,61))
movie_final['Scoregroup'][idx] = 2
idx = movie_final['metascore'].isin(range(61, 81))
movie_final['Scoregroup'][idx] = 3
idx = movie_final['metascore'].isin(range(81, 101))
movie_final['Scoregroup'][idx] = 4

plt.hist(movie_final['Scoregroup'], bins = range(6))
plt.xticks(range(5))
plt.xlim([0, 5])