import requests
from collections import Counter
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
resp = requests.get(BASE_USAJOBS_URL, params = {"CountrySubdivision": 'California', 'NumberOfJobs': 250})
data = resp.json()

organization = []
for job in data['JobData']:
    organization.append(job['OrganizationName'])

result_dict = Counter(organization)
print (result_dict)


