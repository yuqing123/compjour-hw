import requests
import json
url = 'https://open.whitehouse.gov/resource/i9g8-9web.json'
data = json.loads(requests.get(url).text)

total = 0
for d in data:
	result = float(d['salary'])
	total =+ result
	#print(total)
print(total)