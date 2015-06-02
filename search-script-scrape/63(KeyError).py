import requests
import json
url = 'https://data.medicare.gov/resource/g6vv-u9sr.json'
data = json.loads(requests.get(url).text)

total = 0
for d in data:
	result = int(d['fine_amount'])
	#print(result)
	total =+ result
print(total)