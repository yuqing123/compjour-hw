import requests
from lxml import html
response = requests.get('http://www.asias.faa.gov/pls/apex/f?p=100:93:0::NO:::')
doc = html.fromstring(response.text) 
tables = doc.cssselect('table')[1]
first_row = tables.cssselect('tr')[1]
print(first_row.text_content())