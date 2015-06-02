from lxml import html
import requests
page = requests.get('http://www.fda.gov/ICECI/Inspections/ucm381526.htm')
tree = html.fromstring(page.text)
result = tree.xpath('//table[@summary="Foods"]/tbody/tr/td/text()')[3]
print (result)