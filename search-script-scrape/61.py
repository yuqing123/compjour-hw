from lxml import html
import requests
page = requests.get('http://www.state.gov/secretary/travel/')
tree = html.fromstring(page.text)
result = tree.xpath('//li[@id="total-mileage"]/span/text()')
print (result)