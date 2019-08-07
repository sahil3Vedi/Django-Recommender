# movie csv desired format: movieId - Title - Genres - Year
# Current format: movieId - Title(Year) - Genres

import pandas as pd
import os

DATA_DIR = "ml-latest-small"
filename = "movies.csv"
PATH = os.path.join(DATA_DIR, filename)

data = pd.read_csv(PATH)
# 9742 rows and 3 columns in the original data frame at present

datalen = len(data)


# new DataFrame identical in dimension to the original one
newDF = pd.DataFrame(data=None, columns=["year"], index=data.index)
genreDF = pd.DataFrame(data=None, columns=["genres"], index=data.index)

# defining function that returns year from a movie string

def getYear(title):
    if (title[0] == '"') or (title[0] == "'"):
        intitle = title[1:-1]
    else:
        intitle = title
    year = intitle[-5:-1]
    return year

yearindex = 0
for i in data["title"]:
    newDF["year"][yearindex] = getYear(i)
    yearindex += 1

genreindex=0
for j in data["genres"]:
    x=j.split("|")
    genrestring = x[0]
    firstlength = len(genrestring)
    for g in x:
        genrestring += str("," + g)
    genrestring = genrestring[firstlength + 1:]
    genreDF["genres"][genreindex] = genrestring
    genreindex += 1

data["year"] = newDF
data["genres"] = genreDF

# We need to remove rows that have non numeric year fields as this can impact the KNN algorithm.

rowindex=0
for row in data:
    if data["year"][rowindex].isnumeric:
        rowindex += 1
    else:
        data.drop(data.index[rowindex])


newcsv = "movies-refined.csv"
NEW_PATH = os.path.join(DATA_DIR, newcsv)

# Now we have created a DataFrame in the desired format. We will export the DataFrame to a new CSV File

data.to_csv(path_or_buf=NEW_PATH)

# once the movies-refined.csv file is created, the developer still needs to go through the csv file on excel and remove data with incorrect or invalid labels.





