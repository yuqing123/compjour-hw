from lxml import html
import requests
page = requests.get('http://clinicalstudies.info.nih.gov/cgi/protinstitute.cgi?NIAAA.0.html')
tree = html.fromstring(page.text)
database = tree.xpath('//dl')
print (len(database))