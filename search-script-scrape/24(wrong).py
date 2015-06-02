from lxml import html
import requests
response = requests.get('http://www.nyclu.org/content/stop-and-frisk-data')
doc = html.fromstring(response.text)
link = doc.cssselect('ul li')[1]
print(link.text)