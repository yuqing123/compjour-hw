import requests
import json
url = 'https://analytics.usa.gov/data/live/ie.json'
data = json.loads(requests.get(url).text)
ie6 = data['totals']['ie_version']['6.0']
print(ie6)
