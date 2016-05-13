# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:26:58 2016

@author: OUJ070
"""
# Names of columns
meta_movies_df.columns.values
mojo_movies_df.columns.values

# total elements and structure of Meta Critic data
meta_movies_df.size
meta_movies_df.shape

# total elements and structure of Mojo
mojo_movies_df.size
mojo_movies_df.shape


g = movie_final.columns.to_series().groupby(movie_final.dtypes).groups

pd.value_counts(movie_final.director_meta.unique())

movie_final.studio.unique()

movie_final.Scoregroup.unique()

a = movie_final.studio.unique()
a.sort_index()