import requests
BASE_USAJOBS_URL = "https://data.consumerfinance.gov/api/views"
product = 'student loan'
atts = {"Keyword": jobname, 'NumberOfJobs': 1}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
print(data['TotalJobs'])