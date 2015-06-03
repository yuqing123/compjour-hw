import requests
from lxml import html
response = requests.get('http://www.bls.gov/oes/current/oes291041.htm')
doc = html.fromstring(response.text) 
tables = doc.cssselect('table')
t = tables[1]
td = t.cssselect('td')[2]
print(td.text)

