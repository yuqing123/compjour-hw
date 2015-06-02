import requests
from lxml import html
response = requests.get('http://www.bls.gov/oes/current/oes291041.htm')
doc = html.fromstring(response.text) 
last_row = doc.cssselect('tr')[1]
#print(last_row)
td = last_row.cssselect('td')[3]
print(td.text)

