import requests
from lxml import html
response = requests.get('http://dq.cde.ca.gov/dataquest/cohortrates/GradRates.aspx?cds=43000000000000&TheYear=2013-14&Agg=O&Topic=Dropouts&RC=County&SubGroup=Ethnic/Racial')
doc = html.fromstring(response.text) 
row = doc.cssselect('tr')[1]
td = row.cssselect('td')[6]
print(td.text)