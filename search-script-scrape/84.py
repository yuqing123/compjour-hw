from lxml import html
import requests
page = requests.get('https://www.federalregister.gov/')
tree = html.fromstring(page.text)
result = tree.xpath('//ul[@class="statistics"]/li/a/span/text()')[0]
print (result)