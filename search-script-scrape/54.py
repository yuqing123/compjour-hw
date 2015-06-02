from lxml import html
import requests
page = requests.get('http://www.fbi.gov/wanted/wcc/@@wanted-group-listing')
tree = html.fromstring(page.text)
result = tree.xpath('//div[@class="wanted-person-container-wrapper"]')
print (len(result))