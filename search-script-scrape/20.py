import requests
from lxml import html
response = requests.get('https://www.osha.gov/pls/imis/establishment.search?p_logger=1&establishment=Wal-Mart&State=CA&officetype=all&Office=all&p_case=all&p_violations_exist=all&startmonth=01&startday=01&startyear=2014&endmonth=05&endday=31&endyear=2015')
doc = html.fromstring(response.text) 
last_row = doc.cssselect('tr')[-1]
#print(last_row)
td = last_row.cssselect('td')[1]
print(td.text)