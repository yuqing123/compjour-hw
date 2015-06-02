from lxml import html
import requests
page = requests.get('http://www.nyclu.org/content/stop-and-frisk-data')
tree = html.fromstring(page.text)
database = tree.xpath('//ul/li/text()')[-15]
print (database)