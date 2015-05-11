import json
import os
import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
CODES_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
sdata = requests.get(CODES_URL).json()
mylist = []
for state in sdata:
    print("Getting:", state)
    atts = {'CountrySubDivision': state,  'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    jobcount = int(data['TotalJobs'])
    mylist.append([state, jobcount])
os.makedirs("data-hold", exist_ok = True)
f = open("data-hold/domestic-jobcount.json", 'w')
f.write(json.dumps(mylist, indent = 2))
f.close()

