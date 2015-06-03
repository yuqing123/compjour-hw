import requests
import json
url = 'https://data.medicare.gov/resource/g6vv-u9sr.json'
data = json.loads(requests.get(url).text)

total = 0
for d in data:
	result = int(d.get('fine_amount', 0))
	#print(result)
	total += result

print(total)