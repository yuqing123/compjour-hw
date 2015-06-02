import requests
from lxml import html
response = requests.get('http://www.asias.faa.gov/pls/apex/f?p=100:93:0::NO:::')
doc = html.fromstring(response.text) 
last_row = doc.cssselect('tr')[1]
#print(last_row)
td = last_row.cssselect('td')[0]
print(td.text)