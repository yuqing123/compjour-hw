from lxml import html
import requests
page = requests.get('https://www.us-cert.gov/ncas/bulletins/SB15-152')
tree = html.fromstring(page.text)
result = tree.xpath('//tr/td/text()')

newlist = []
x = 'ibm'
res = [y for y in result if x in y]
print (len(res))