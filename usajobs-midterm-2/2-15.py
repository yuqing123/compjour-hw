import json
import requests
import os
from collections import Counter
from operator import itemgetter
with open("sample-geochart-cities.html") as f:
    htmlstr = f.read()

CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy...")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jobs = json.loads(rawdata)['jobs']

def get_ca_cities(job):
    locations_list = []
    locs = job['Locations'].split(';')
    for loc in locs:
        cities = loc.split(', ')    
        if (cities[-1] == 'California'):            
            locations_list.append(cities[0].strip())
    return locations_list

c=Counter()
for job in jobs:
    locations_list = get_ca_cities(job)
    c_tmp = Counter(locations_list)
    c=c+c_tmp
    
result=[ [key, c[key]] for key in c.keys() ]

sorteddata = sorted(result, key = itemgetter(1), reverse = True)

chartdata = [['State', 'Jobs']]
chartdata.extend(sorteddata)

tablerows = []
for d in sorteddata:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

tablerows = "\n".join(tablerows)

with open("2-15.html", "w") as f:
    htmlstr = htmlstr.replace('#CHART_DATA#', str(chartdata))
    htmlstr = htmlstr.replace('#TABLE_ROWS#', tablerows)
    f.write(htmlstr)
