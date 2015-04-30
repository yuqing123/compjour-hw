import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
countries = ['China', 'South Africa', 'Tajikistan']
TotalJobs=0
for c in countries:
    atts = {"Country": c, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    
    print("%s has %s job listings." % (c, data['TotalJobs']))
    TotalJobs+=int(data['TotalJobs'])
print("Together, they have %s total job listings." % (TotalJobs))