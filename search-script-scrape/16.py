import requests
BASE_USAJOBS_URL = "https://projects.propublica.org/nonprofits/api/v1/search.json"
order = 'revenue'
sort_order = 'desc'
atts = {"order": order, "sort_order": sort_order}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
print(data['filings'][0]['totrevenue'])