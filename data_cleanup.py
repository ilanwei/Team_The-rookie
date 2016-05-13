# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:42:50 2016

@author: OUJ070
"""
mojo_movies_df['title_cln'] = mojo_movies_df['title']
meta_movies_df['title_cln'] = meta_movies_df['title']

def clean(dataframe, columnname):
    dataframe[columnname].replace("\\.", "",inplace=True, regex = True)
    dataframe[columnname].replace(",", "",inplace=True, regex = True)
    dataframe[columnname].replace(":", "",inplace=True, regex = True)
    dataframe[columnname].replace("'", "",inplace=True, regex = True)
    dataframe[columnname].replace("!", "",inplace=True, regex = True)
    dataframe[columnname].replace("-", "",inplace=True, regex = True)
    dataframe[columnname].replace("\\?", "",inplace=True, regex = True)
    dataframe[columnname].replace("\([^)]*\)", "",inplace=True, regex = True)
    dataframe[columnname].replace(" ", "",inplace=True, regex = True)
    dataframe[columnname]= dataframe[columnname].str.lower()
    
clean(mojo_movies_df, 'title_cln')
clean(meta_movies_df, 'title_cln')

mojo_clean = mojo_movies_df[pd.notnull(mojo_movies_df['title_cln'])]
meta_clean = meta_movies_df[pd.notnull(meta_movies_df['title_cln'])]

movie_db = pd.merge(mojo_clean, meta_clean, on = 'title_cln', suffixes = ('_mojo', '_meta'), how = 'outer')

movie_db['user_score'] = movie_db['user_score'].convert_objects(convert_numeric=True)

keepers = ['domestic_gross', 'opening_per_theater', 'opening_weekend_take', 'production_budget', 'title_cln', 'widest_release', 'worldwide_gross', 'year_meta', 'year_mojo', 'director_meta', 'genre', 'metascore', 'num_critic_reviews', 'num_user_ratings', 'num_user_reviews', 'rating', 'release_date', 'runtime_minutes', 'studio', 'user_score']

movie_final = movie_db[keepers]
