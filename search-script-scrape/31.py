import requests
import json
url = 'http://api.data.gov:80/regulations/v3/documents.json?api_key=DEMO_KEY&countsOnly=1&rpp=1000&cs=3'
data = json.loads(requests.get(url).text)
print (data['totalNumRecords'])