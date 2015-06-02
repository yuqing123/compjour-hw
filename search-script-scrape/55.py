from lxml import html
import requests
page = requests.get('http://www.gao.gov/browse/topic')
tree = html.fromstring(page.text)
result = tree.xpath('//ul[@class="column"]/li/span/text()')[-2]
print (result)