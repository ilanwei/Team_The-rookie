# -*- coding: utf-8 -*-
"""
@author: ouj070
Project 1
@Date: May 11th 2016
@Team: Team_Rookie
"""

# libraries / packages
import os
import json
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
# constants
BASE_DIR = "C://Users/ouj070/Documents/GitHub/ct16_cap1_ds5/project_1/data"
MOJO_DIR = os.path.join(BASE_DIR, 'boxofficemojo')
META_DIR = os.path.join(BASE_DIR, 'metacritic')

# Create DataFrame

movies = []

NameList = [name for name in os.listdir(MOJO_DIR) if ".json" in name] 
# to avoid any non json file related failure

for i in NameList:
    target_file_path = os.path.join(MOJO_DIR, i)
    with open(target_file_path, 'r') as target_file:
        movie = json.load(target_file)
        movies.append(movie)

mojo_movies_df = pd.DataFrame(movies)
print len(movies)

NameList = [name for name in os.listdir(META_DIR) if ".json" in name] 
movies = []

for i in NameList:
    target_file_path = os.path.join(META_DIR, i)
    with open(target_file_path, 'r') as target_file:
        movie = json.load(target_file)
        if type(movie) is not dict:
            continue
        else:
            movies.append(movie)

meta_movies_df = pd.DataFrame(movies)
print len(movies)

mojo_movies_df['title_cln'] = mojo_movies_df['title']
meta_movies_df['title_cln'] = meta_movies_df['title']

def clean(dataframe, columnname):
    dataframe[columnname].replace("\\.", "",inplace=True, regex = True)
    dataframe[columnname].replace(",", "",inplace=True, regex = True)
    dataframe[columnname].replace(":", "",inplace=True, regex = True)
    dataframe[columnname].replace("'", "",inplace=True, regex = True)
    dataframe[columnname].replace("!", "",inplace=True, regex = True)
    dataframe[columnname].replace("-", "",inplace=True, regex = True)
    dataframe[columnname].replace("?", "",inplace=True, regex = True)
    dataframe[columnname].replace("\([^)]*\)", "",inplace=True, regex = True)
    dataframe[columnname].replace(" ", "",inplace=True, regex = True)
    dataframe[columnname]= dataframe[columnname].str.lower()
    
clean(mojo_movies_df, 'title_cln')
clean(meta_movies_df, 'title_cln')

mojo_clean = mojo_movies_df[pd.notnull(mojo_movies_df['title_cln'])]
meta_clean = meta_movies_df[pd.notnull(meta_movies_df['title_cln'])]

movie_db = pd.merge(mojo_clean, meta_clean, on = 'title_cln', suffixes = ('_mojo', '_meta'), how = 'outer')

keepers = ['domestic_gross', 'opening_per_theater', 'opening_weekend_take', 'production_budget', 'title_cln', 'widest_release', 'worldwide_gross', 'year_meta', 'year_mojo', 'director_meta', 'genre', 'metascore', 'num_critic_reviews', 'num_user_ratings', 'num_user_reviews', 'rating', 'release_date', 'runtime_minutes', 'studio', 'user_score']

movie_final = movie_db[keepers]

# start model exploration
pd.value_counts(movie_final.director_meta.unique())

a = movie_final.studio.unique()

backup = movie_final.copy()

g = movie_final.columns.to_series().groupby(movie_final.dtypes).groups

# Create Month Variable

movie_final['month'] = pd.DataFrame([pd.to_datetime(date) for date in movie_final['release_date']])

movie_final['month'] = movie_final['month'].dt.month

plt.hist(movie_final['month'])

a = movie_final['month'].dropna()

plt.hist(a)

# opt1: use a mapper
# opt2: Create a T/F indicator by using isin
# opt3: use replace

movie_final['Season'] = 0
idx = movie_final['month'].isin([2,3,4])
movie_final['Season'][idx] = 1
idx = movie_final['month'].isin([5,6,7])
movie_final['Season'][idx] = 2
idx = movie_final['month'].isin([8,9,10])
movie_final['Season'][idx] = 3
idx = movie_final['month'].isin([11,12,1])
movie_final['Season'][idx] = 4

plt.hist(movie_final['Season'])
