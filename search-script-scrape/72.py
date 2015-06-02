import requests
import json
url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson'
data = json.loads(requests.get(url).text)
quakes = data['features']
print(len(quakes))