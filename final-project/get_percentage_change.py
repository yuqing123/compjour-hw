import pandas as pd
import csv

a = pd.read_csv("./data/YA_1980_050.csv")
b = pd.read_csv("./data/YA_2009_2013_050.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='fips')
merged.to_csv("./data/tmp.csv", index=False)

with open('./data/tmp.csv','r') as csvinput:
    with open('./data/percentage_change.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('percentage_change')
        all.append(row)

        for row in reader:
            row.append(float(row[113])-float(row[58]))
            all.append(row)

        writer.writerows(all)