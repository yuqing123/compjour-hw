import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
states = ['California', 'Florida', 'New York', 'Maryland']
dict = {}
for s in states:
    atts = {"CountrySubdivision": s, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    value = int(data['TotalJobs'])
    dict[s] = value
print (dict)



