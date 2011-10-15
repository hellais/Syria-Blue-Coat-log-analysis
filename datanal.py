#!/usr/bin/env python

import csv

cread = csv.reader(open('recurrency-table-expo.csv','r'),delimiter=",")

catcount = []
uniq = []
uniq_count = []
for row in cread:
    for i in row[1].split(","):
        if i not in uniq:
            uniq.append(i)
        catcount.append((row[0],i))

for i in uniq:
    tmp = 0
    for y in catcount:
        if i in y:
            tmp += int(y[0])
            print "%s: %s" % (y[0], y[1])
    uniq_count.append((i,tmp))
fp = open('uniq-counts.csv','w')
for x in uniq_count:
    fp.write(str(x[0].strip()) + ", " + str(x[1]) + "\n")

fp.close()



#print catcount
