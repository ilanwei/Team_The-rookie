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

# Create Seasons
movie_final['Season'] = np.nan
idx = movie_final['month'].isin([2,3,4])
movie_final['Season'][idx] = 1
idx = movie_final['month'].isin([5,6,7])
movie_final['Season'][idx] = 2
idx = movie_final['month'].isin([8,9,10])
movie_final['Season'][idx] = 3
idx = movie_final['month'].isin([11,12,1])
movie_final['Season'][idx] = 4

new_list=['season_1','season_2','season_3','season_4']
movie_final[new_list]=pd.get_dummies(movie_final['Season'], prefix = 'Season')