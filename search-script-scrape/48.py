import requests
import json
url = 'https://open.whitehouse.gov/resource/i9g8-9web.json'
data = json.loads(requests.get(url).text)

total = 0
for d in data:
	result = float(d['salary'])
	total += result
a = total
#print(a)

url = 'https://open.whitehouse.gov/resource/rcp4-3y7g.json'
data = json.loads(requests.get(url).text)

total = 0
for d in data:
	result = float(d['salary'])
	total += result
b = total
#print(b)

print (a-b)