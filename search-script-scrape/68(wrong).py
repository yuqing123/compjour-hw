import requests
from lxml import html
response = requests.get('https://www.accessdata.fda.gov/scripts/cder/ob/docs/tempah.cfm')
doc = html.fromstring(response.text) 
tables = doc.cssselect('table')[0]

row = tables.cssselect('tr')
print (len(row))