from lxml import html
import requests
page = requests.get('http://www.fda.gov/MedicalDevices/Safety/ucm384618.htm')
tree = html.fromstring(page.text)
foodrecall = tree.xpath('//linktitle')
print (len(foodrecall))