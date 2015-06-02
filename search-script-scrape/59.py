from lxml import html
import requests
page = requests.get('http://catalog.data.gov/dataset?q=university')
tree = html.fromstring(page.text)
result = tree.xpath('//div[@class="new-results"]/text()')[-2]
print (result)

