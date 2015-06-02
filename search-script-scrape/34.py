
from lxml import html
import requests
page = requests.get('http://www.accessdata.fda.gov/scripts/enforcement/enforce_rpt-Product-Tabs.cfm?action=Expand+Index&w=05272015&lang=eng')
tree = html.fromstring(page.text)
foodrecall = tree.xpath('//tr[@class="Food"]')
print (len(foodrecall))