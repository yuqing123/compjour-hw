from lxml import html
import requests
page = requests.get('http://www.regulations.gov/#!docketDetail;D=FDA-2015-N-0540')
tree = html.fromstring(page.text)
result = tree.xpath('//span[@id="commentsShow"]/span[@class="GCARQJCDBWD"]/span/text()')
print (result)