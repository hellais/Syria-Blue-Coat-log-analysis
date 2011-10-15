import csv

csv_reader = csv.reader(open('uniq-counts-export.csv', 'rb'), delimiter=',')

sum = 0
for row in csv_reader:
    sum += int(row[1])

csv_reader = csv.reader(open('uniq-counts-export.csv', 'rb'), delimiter=',')

for row in csv_reader:
    percent = float(row[1])/sum*100
    print "['%s', %s]," % (row[0], percent)

