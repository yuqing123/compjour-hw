import csv
import requests
from io import StringIO
CSVURL = 'https://www.osha.gov/dep/fatcat/fy15_federal-state_summaries.csv'
response = requests.get(CSVURL)
data = csv.DictReader(StringIO(response.text))
rows = list(data)
print (len(rows))

#101
#import csv
#import requests
#from io import StringIO
#CSVURL = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
#response = requests.get(CSVURL)
#data = csv.DictReader(StringIO(response.text))
#rows = list(data)
#len([i for i in rows if i['gender'] == 'F' and i['in_office'] == '1'])