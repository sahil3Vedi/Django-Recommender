# calculate correlation of a given movie along with string matching

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

print("Enter Any Movie: ")

movie = str(input())

# ------ Step 1: String Matching

results = []
movrefid = 0
for moviename in movdata["title"]:
    if movie in moviename:
        results.append(moviename)

#print("Closest Results:")
#printcount = 1
#for result in results:
#    print(str(printcount) + ". " + result)
#    printcount += 1

movie = results[0]
print("Selected Movie: " + movie)

# distance matrix will store distance values for all values of parameter Yc.
# d = sqrt(deltaX**2 + Cy*(deltaY**2))

def deltaX(x1,x2):
    return abs(x1-x2)

def deltaY(y1,y2):
    denom = len(y2)
    num = 0
    for y in y2:
        if y in y1:
            num+=1
    return 1-(num/denom)

# def distance(id1,id2):


# ------- Step 2: Calculating Correlation

