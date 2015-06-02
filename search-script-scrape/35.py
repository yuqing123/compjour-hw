from lxml import html
import requests
page = requests.get('https://data.ny.gov/browse?sortBy=most_accessed&sortPeriod=month&utf8=%E2%9C%93')
tree = html.fromstring(page.text)
result = tree.xpath('//div[@class="titleLine"]/span[@class="hide"]/text()')[0]
print (result)