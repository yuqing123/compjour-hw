import requests
import json
url = 'https://analytics.usa.gov/data/live/top-pages-realtime.json'
data = json.loads(requests.get(url).text)
mains = data['data']

def visitor(main):
    return float(main['active_visitors'])

d = max(mains, key = visitor)
print(d['page'])