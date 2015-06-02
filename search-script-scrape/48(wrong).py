import requests
import json
url_2014 = 'https://open.whitehouse.gov/resource/i9g8-9web.json'
url_2010 = 'https://open.whitehouse.gov/resource/rcp4-3y7g.json'
data = json.loads(requests.get(url).text)

print (data[0]['salary'])