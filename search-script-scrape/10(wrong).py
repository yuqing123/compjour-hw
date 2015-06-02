import csv
with open('./data-hold/2010_City.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)