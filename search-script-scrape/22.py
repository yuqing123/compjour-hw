import requests
BASE_USAJOBS_URL = "http://congress.api.sunlightfoundation.com/committees"
bioid = 'B000711'
apikey = '5c5f3b88c5ba45ccba3df232c09d68dc'
atts = {"member_ids": bioid, "apikey": apikey}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
print(data['count'])