import csv
import requests
from io import StringIO
CSVURL = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
response = requests.get(CSVURL)
data = csv.DictReader(StringIO(response.text))
rows = list(data)
print (len([i for i in rows if i['twitter_id'] is not ""]))