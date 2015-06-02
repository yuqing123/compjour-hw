from lxml import html
import requests
page = requests.get('https://www.nsa.gov/research/publications/')
tree = html.fromstring(page.text)
result = tree.xpath('//table[@class="dataTable"]/tr')
print (len(result)-1)