import requests
import json
url = 'https://analytics.usa.gov/data/live/realtime.json'
data = json.loads(requests.get(url).text)
now = data['data'][0]['active_visitors']
print(now)
