import csv
import sys
import json
import requests

#EDIT THIS LIST WITH YOUR REQUIRED JSON KEY NAMES

WANTEDHEADERS = ['population18To34_p','neverMarried_p','liveWithParent_p','educationBachelor_p','employed_p']

def convert(csv_filename):
    print ("Opening CSV file: ",csv_filename)
    f = open(csv_filename, 'r', encoding = 'utf-8')
    csv_reader = csv.DictReader(f)
    csvdata = list(csv_reader)
    newdata = []

    for row in csvdata:
        d = {}
        newdata.append(d) 
        d['fips'] = row['fips']
        d['name'] = row['name']
        for col in WANTEDHEADERS:
            d[col] = float(row[col]) if row[col] is not "" else 0



    # save the data
    json_filename = "./jsons/%s.json" % csv_filename.split(".")[0]

    with open(json_filename,'w') as jsonf:
        print ("Saving JSON to file: ",json_filename)
        jsondata = json.dumps(newdata, indent = 2)
        jsonf.write(jsondata) 


convert('YA_2009_2013_040.csv')


### trim the data

with open("./jsons/YA_2009_2013_040.json") as f:
    data = json.loads(f.read())

thelist = []
for d in data:
    thelist.append([d['name'],d['population18To34_p'],d['liveWithParent_p'],d['neverMarried_p'],d['educationBachelor_p'],d['employed_p']])
print (thelist)





