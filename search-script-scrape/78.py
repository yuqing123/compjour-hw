from lxml import html
import requests
page = requests.get('https://services.sccgov.org/facilityinspection/Closure/Index?sortField=sortbyEDate')
tree = html.fromstring(page.text)
result = tree.xpath('//td[@class="text-left"]/a/text()')
newlist = []
x = 'CUPERTINO'
res = [y for y in result if x in y]
print (len(res))