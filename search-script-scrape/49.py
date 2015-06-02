import requests
BASE_USAJOBS_URL = "http://congress.api.sunlightfoundation.com/bills"
bioid = 'P000197'
vetoed = True
apikey = '5c5f3b88c5ba45ccba3df232c09d68dc'
atts = {"sponsor_id": bioid, "history.vetoed":vetoed, "apikey": apikey}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
print (len(data['results']))