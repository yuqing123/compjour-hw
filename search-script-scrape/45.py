from lxml import html
import requests
page = requests.get('https://www.us-cert.gov/ncas/alerts')
tree = html.fromstring(page.text)
result = tree.xpath('//div[@class="item-list"]/ul/li')
print (len(result))