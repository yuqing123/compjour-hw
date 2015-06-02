from lxml import html
import requests
page = requests.get('https://clinicaltrials.gov/')
tree = html.fromstring(page.text)
database = tree.xpath('//div[@id="trial-count"]/p/span[@class="highlight"]/text()')[0]
print (database)