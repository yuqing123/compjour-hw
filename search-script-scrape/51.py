import requests
from lxml import html
response = requests.get('http://www.supremecourt.gov/opinions/slipopinions.aspx')
doc = html.fromstring(response.text) 
tables = doc.cssselect('table')

t = tables[1]
td = t.cssselect('td')[3]
print(td.text_content())

