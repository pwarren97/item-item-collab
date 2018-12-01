#!/usr/bin/python
import pandas as pd
import numpy as np
import math

data_full = pd.read_csv("data/data-full.csv", names=["MovieID", "UserID", "Rating"])
movie_names = pd.read_csv("data/movie_names.csv", error_bad_lines=False, names=["MovieID", "YearOfRelease", "Title"])

# creates a new table out of data_full with the means of the ratings in place of Rating
Mean = data_full.groupby(["MovieID"], as_index=False, sort=False).mean().rename(columns = {'Rating': 'Mean_Rating'})
Mean = Mean.drop('UserID', 1)

# create a ratings table that includes the mean of the ratings in a column
Ratings = pd.merge(data_full, Mean, on='MovieID', how='left', sort=False)
# print Ratings


movie_data_all_append = pd.DataFrame()

user_data = Ratings[Ratings['UserID'] != 320]
distinct_movies = np.unique(suer_data['MovieID'])
i = 1
for movie in distinct_movies:
    if i%10 == 0:

    print i, "out of ", len(distinct_movies)

    movie_data_all=pd.DataFrame()

    movie_data = Ratings[Ratings['MovieID']==movie]

    movie_data = movie_data[['UserID', 'MovieID', 'rating_adjusted']].drop_duplicates()
    movie_data = movie_data.rename(columns={'rating_adjusted':'rating_adjusted1'})
    movie_data = movie_data.rename(columns={'MovieID':'MovieID1'})
    movie1_val = np.sqrt(np.sum(np.square(movie_data['rating_adjusted1']), axis=0))
    user_data1 = Ratings[Ratings['UserID']==320]