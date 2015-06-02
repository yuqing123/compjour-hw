from lxml import html
import requests
page = requests.get('https://www.phillypolice.com/ois/')
tree = html.fromstring(page.text)
result = tree.xpath('//tr/td/a/text()')
print (len(result))