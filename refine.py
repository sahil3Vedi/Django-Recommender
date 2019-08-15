# ------ Purpose of this code: Iterate through movies-refined.csv and ratings.csv and find out common movie IDs.
# ------ Prepare a separate dataframe and csv file for these movies
# ------ Final Format: movieId, title, genres, year

import pandas as pd
import os

DATA_DIR = "ml-latest-small"
reviewscsv = "ratings.csv"
moviescsv = "movies-refined.csv"
REV_PATH = os.path.join(DATA_DIR, reviewscsv)
MOV_PATH = os.path.join(DATA_DIR, moviescsv)

movdata = pd.read_csv(MOV_PATH)
movdatalen = len(movdata)
revdata = pd.read_csv(REV_PATH)
revdatalen = len(revdata)

print(str(movdatalen) + " entries inside movies dataframe")
print(str(revdatalen) + " entries inside reviews dataframe")


# movieIds is list of all the movieIds featured on both movdata and revdata
movieIDs = []
repeats = 0
voidrepeat = 0
voidslist = []
# check whether each movieId referenced in revData actually exists in in movData["movieId"]. If it exists then add to the movieIds list
for id in revdata["movieId"]:
    if id in movieIDs:
        repeats += 1
    else:
        if id in movdata["movieId"]:
            movieIDs.append(id)
        else:
            if id in voidslist:
                voidrepeat += 1
            else:
                voidslist.append(id)

print(len(voidslist))
print(len(movieIDs))

movieframe= []

for movindex in range (len(movdata)):
    selection = movdata.iloc[movindex]
    if selection["movieId"] in movieIDs:
        aselec = selection["movieId"]
        bselec = selection["title"]
        cselec = selection["genres"].split(",")
        dselec = selection["year"]
        packselec = [aselec,bselec,cselec,dselec]
        movieframe.append(packselec)

moviedataframe = pd.DataFrame(movieframe, columns=['movieId','title','genres','year'])

newcsv = "featured-movies.csv"
NEW_PATH = os.path.join(DATA_DIR, newcsv)

#code omitted for safety
#moviedataframe.to_csv(path_or_buf=NEW_PATH)

#print("Export Complete!")


