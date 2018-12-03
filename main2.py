#!/usr/bin/python
import csv
import math

# k is for the kNN part of this
k = 3

# returns a 3 item list, concatenating the movie name back in one piece when it is split up by a comma
def load_data(filename):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        lines = list(lines)
        for row in lines:
            row[2] = ''.join(row[2:])
            del row[3:]
        return lines


# load each of the CSV files
data_full = load_data('./data/data-full.txt')
movie_names = load_data('./data/movie_names.txt')


def get_means(data_full):
    id_mean_list = []
    current_movie_id = 0
    sum = 0
    counter = 0

    for row in data_full:
        # if you are looking at a rating of the same movie as the last one,
        # just add this rating to the sum and increment the counter
        if current_movie_id == row[0]:
            sum = sum + float(row[2])
            counter = counter + 1
        else:
            # If you are not at the beginning of a group of ratings for a movie,
            # add the movie_id and mean to the id_mean_list
            if not current_movie_id == 0:
                id_mean_list.append([current_movie_id, (sum/counter)])

            # set the current_movie_id to the new one and reset the sum
            current_movie_id = row[0]
            sum = float(row[2])
            counter = 1
    # return list of type [[movieID, mean]]
    return id_mean_list

# used to add the years for movies onto a list,
# in this case so that the mean ratings and the year
# to calculate distance with
def append_years(user_list, movie_names):
    for item in user_list:
        idx_of_movie = int(item[0])-1
        item.append(movie_names[idx_of_movie][1])


movie_means = get_means(data_full)
append_years(movie_means, movie_names)

def get_top_k(user_list):
    top_k = []
    for item in user_list:
        

