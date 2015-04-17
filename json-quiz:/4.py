import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json"
data = json.loads(requests.get(data_url).text)

print('A.', len(data['artists']))
print('B.',data['artists'][4]['name'])
print('C.',data['artists'][11]['followers']['total'])
a = data['artists'][0]['genres']
print('D.', ', '.join(a))
print('E.',data['artists'][19]['images'][0]['url'])