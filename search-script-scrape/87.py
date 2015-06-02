from lxml import html
import requests
page = requests.get('https://instagram.com/tsa/')
tree = html.fromstring(page.text)
result = tree.xpath('//li[@class="sStat"]/span[@class="sCount"]/text()')
print (result)