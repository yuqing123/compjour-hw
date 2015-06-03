import requests
from lxml import html
response = requests.get('http://www.dallaspolice.net/ois/ois.html')
doc = html.fromstring(response.text) 
tables = doc.cssselect('table')[1]
row = tables.cssselect('tr')

for r in row:
	td = r.cssselect('td')[3]
	print(td.text)