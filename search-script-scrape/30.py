import requests
from lxml import html
response = requests.get('http://www.dc.state.fl.us/oth/deathrow/execlist.html')
doc = html.fromstring(response.text) 
last_row = doc.cssselect('tr')[-1]
#print(last_row)
td = last_row.cssselect('td')[0]
print(td.text)