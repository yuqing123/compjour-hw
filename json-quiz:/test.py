import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json"
data = json.loads(requests.get(data_url).text)

artis
for i in data
print i