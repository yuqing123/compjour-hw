import time
import requests
from lxml import html
response = requests.get('https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html')
doc = html.fromstring(response.text) 
last_row = doc.cssselect('tr')[1]
#print(last_row)
td = last_row.cssselect('td')[0]
#print(td.text)
#print (time.strptime(td.text, "%m/%d/%Y")[7])

schedule = time.strptime(td.text, "%m/%d/%Y")[7]
#print (schedule)
current = time.strftime("%j")
#print (current)
print (int(schedule) - int(current))