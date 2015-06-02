import requests
from lxml import html
response = requests.get('http://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk')
doc = html.fromstring(response.text) 
third_row = doc.cssselect('tr')[2]
td = third_row.cssselect('td')[6]
print(td.text)
