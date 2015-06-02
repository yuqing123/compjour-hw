import csv
import requests
from io import StringIO
CSVURL = 'https://www.osha.gov/dep/fatcat/fy15_federal-state_summaries.csv'
response = requests.get(CSVURL)
data = csv.DictReader(StringIO(response.text))
rows = list(data)
print (len(rows))

