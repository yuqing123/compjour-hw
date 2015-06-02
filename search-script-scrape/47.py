from lxml import html
import requests
page = requests.get('http://travel.state.gov/content/passports/english/alertswarnings.html')
tree = html.fromstring(page.text)
result = tree.xpath('//td[@class="alert"]')
print (len(result))