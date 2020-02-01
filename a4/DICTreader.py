#author: Sebastian Feldam

import csv
ramenRatings = []   #empty list
rowCount = 0

#opens the csv file
with open('complete.csv', 'r') as csv_fi:
    #converts to a reader object
    reader = csv.DictReader(csv_fi)

    #reader object loop
    for ramenRowD in reader:
        rowCount += 1
        ramenRatings.append(ramenRowD)

        if rowCount <= 10:
            print('({0:>5})  co: {1:<15}  brand: {2:<20}  rating: {3:<10}'.format(
            rowCount, ramenRowD['Country'], ramenRowD['Brand'], ramenRowD['Stars']))

print('There are ' + str(len(ramenRatings)) + " rows.")
