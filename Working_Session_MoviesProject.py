# -*- coding: utf-8 -*-
"""
@author: ouj070
Project 1
@Date: May 11th 2016
@Team: Team_Rookie
"""

# libraries / packages
import re
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import xticks

backup = movie_final.copy()


# Create Month Variable

movie_final['month'] = pd.DataFrame([pd.to_datetime(date) for date in movie_final['release_date']])

movie_final['month'] = movie_final['month'].dt.month

a = movie_final['month'].dropna()

plt.hist(a)

# opt1: use a mapper
# opt2: Create a T/F indicator by using isin
# opt3: use replace

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


backup = movie_final.copy()






