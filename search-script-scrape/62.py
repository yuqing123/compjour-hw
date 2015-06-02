from lxml import html
import requests
base_url = 'http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/'
urllist = ['ucm351864.htm', 'ucm367771.htm', 'ucm376571.htm','ucm391572.htm']

total = 0
for i in urllist:
	page = requests.get(base_url+i)
	tree = html.fromstring(page.text)
	result = tree.xpath('//table/tbody/tr')
	a = len(result)-1
	total += a

print (total)
