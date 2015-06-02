import requests
import json
url = 'https://open.whitehouse.gov/resource/i9g8-9web.json'
data = json.loads(requests.get(url).text)


def salary(x):
    return float(x['salary'])

d = max(data, key = salary)
print(d['salary'])