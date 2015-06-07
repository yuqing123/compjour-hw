import csv
import sys
import json
import requests

#EDIT THIS LIST WITH YOUR REQUIRED JSON KEY NAMES
#fieldnames=["fips","name","population","population18To34","population18To34_me","population18To34_p","population18To34_pme","white","white_me","white_p","white_pme","minority","minority_me","minority_p","minority_pme","neverMarried","neverMarried_me","neverMarried_p","neverMarried_pme","liveAlone","liveAlone_me","liveAlone_p","liveAlone_pme","educationBachelor","educationBachelor_me","educationBachelor_p","educationBachelor_pme","civilian","veteran","veteran_me","veteran_p","veteran_pme","foreignBorn","foreignBorn_me","foreignBorn_p","foreignBorn_pme","otherLanguage","otherLanguage_me","otherLanguage_p","otherLanguage_pme","medianEarnings","medianEarnings_me","povertyUniverse","poverty","poverty_me","poverty_p","poverty_pme","employed","employed_me","employed_p","employed_pme","commuter","droveToWork","droveToWork_me","droveToWork_p","droveToWork_pme","liveWithParent","liveWithParent_me","liveWithParent_p","liveWithParent_pme"]

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


### trimming the data

with open("./jsons/YA_2009_2013_040.json") as f:
    data = json.loads(f.read())

thelist = []
for d in data:
    thelist.append([d['name'],d['population18To34_p'],d['liveWithParent_p'],d['neverMarried_p'],d['educationBachelor_p'],d['employed_p']])
print (thelist)





