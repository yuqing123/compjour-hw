import requests
import json
durl = 'http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json'
data = json.loads(requests.get(durl).text)
quakes = data['features']


basemap_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400'
for q in quakes:
	if q['properties']['mag'] > 6.0
	markers_str = 'markers=color:red'
	for q in quakes:
	    coords = q['geometry']['coordinates']
	    lng = str(coords[0])
	    lat = str(coords[1])
 	   s = '%7C' + lat + ',' + lng
	    markers_str += s
	else
	markers_str = 'markers=color:orange'
	for q in quakes:
	    coords = q['geometry']['coordinates']
	    lng = str(coords[0])
	    lat = str(coords[1])
 	   s = '%7C' + lat + ',' + lng
	    markers_str += s

print('N.', basemap_url + '&' + markers_str) 