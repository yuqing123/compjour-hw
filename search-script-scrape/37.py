from lxml import html
import requests
page = requests.get('https://www.cia.gov/about-cia/leadership')
tree = html.fromstring(page.text)
result = tree.xpath('//div[@class="documentByLine"]/div/text()')[-1]
print (result)