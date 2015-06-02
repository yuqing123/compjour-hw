from lxml import html
import requests
page = requests.get('http://gov.georgia.gov/bills-signed/2015')
tree = html.fromstring(page.text)
result = tree.xpath('//tr[@class="odd views-row-first"]/td/a/text()')[0]
print (result)