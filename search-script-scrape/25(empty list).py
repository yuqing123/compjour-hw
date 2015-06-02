from lxml import html
import requests
page = requests.get('http://www.safercar.gov/Vehicle+Shoppers/5-Star+Safety+Ratings/2011-Newer+Vehicles/Vehicle-Detail?vehicleId=9096')
tree = html.fromstring(page.text)
rating = tree.xpath('//div[@class="frontal_cr"]/img/@scr')
print (rating)