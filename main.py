#!/usr/bin/python
import pandas as pd
import numpy as np
import math

data_full = pd.read_csv("data/data-full.csv", names=["MovieID", "UserID", "Rating"])
movie_names = pd.read_csv("data/movie_names.csv", error_bad_lines=False, names=["MovieID", "YearOfRelease", "Title"])



### IMPLEMENTS collb-flitering.pdf page 35 - finds difference between mean and user rating ###

# creates a new table out of data_full with the means of the ratings in place of Rating column
Mean = data_full.groupby(["MovieID"], as_index=False, sort=False).mean().rename(columns = {'Rating': 'Rating_Mean'})
Mean = Mean.drop('UserID', 1)

# print Mean

# create a ratings table that includes the mean of the ratings in a column
Ratings = pd.merge(data_full, Mean, on='MovieID', how='left', sort=False)
# print Ratings
Ratings['rating_adjusted'] = Ratings['Rating'] - Ratings['Rating_Mean']
print Ratings

### end of finding the difference between mean and user rating ###



# user_id = 320


# movie_data_all_append = pd.DataFrame()

# user_data = Ratings[Ratings['UserID'] != user_id]
# unique_movies = np.unique(user_data['MovieID'])
# i = 1
# for movie in unique_movies:
#     if i%10 == 0:

#     print i, "out of ", len(unique_movies)


# movie_data_all=pd.DataFrame()

# movie_data = Ratings[Ratings['MovieID']==movie]

# movie_data = movie_data[['UserID', 'MovieID', 'rating_adjusted']].drop_duplicates()
# movie_data = movie_data.rename(columns={'rating_adjusted':'rating_adjusted1'})
# movie_data = movie_data.rename(columns={'MovieID':'MovieID1'})
# movie1_val = np.sqrt(np.sum(np.square(movie_data['rating_adjusted1']), axis=0))
# user_data1 = Ratings[Ratings['UserID']==user_id]
