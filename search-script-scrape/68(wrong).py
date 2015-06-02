from lxml import html
import requests
page = requests.get('https://www.accessdata.fda.gov/scripts/cder/ob/docs/tempah.cfm')
tree = html.fromstring(page.text)
result = tree.xpath('//tr/td/a')
print (len(result))