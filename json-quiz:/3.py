import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json"
response = requests.get(data_url)
text = response.text
data = json.loads(text)

result_obj = data['results'][0]
print('A.', result_obj['formatted_address'])
print('B.', data['status'])
print('C.', result_obj['geometry']['location_type'])
geometry_obj = result_obj['geometry']
print('D.', geometry_obj['location']['lat'])
print('E.', geometry_obj['viewport']['southwest']['lng'])
a = result_obj['address_components'][0]['long_name']
b = result_obj['address_components'][1]['long_name']
seq = (a, b)
print('F.', ', '.join(seq))