import requests
import json
import os
data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = "/tmp/congresslist.json"

if os.path.exists(tempfilename):
    tfile = open(tempfilename, "r")
    j = tfile.read()
else:    
    j = requests.get(data_url).text
    tfile = open(tempfilename, "w")
    tfile.write(j)

tfile.close()
accounts = json.loads(j)

print ('A.', len(accounts))

x = 0
for a in accounts:
    if a['followers_count'] > 10000:
        x += 1
print("B.", x)

y = 0
for a in accounts:
	if a['verified'] == True:
		y += 1
print("C.", x)

counts = []
for a in accounts:
    counts.append(a['followers_count'])
maxval = sorted(counts, reverse = True)[0]
print("D.", maxval)

tweets = []
for a in accounts:
	tweets.append(a['statuses_count'])
maxnumber = sorted(tweets, reverse = True) [0]
print("E.", maxnumber)

from operator import itemgetter
y = sorted(accounts, key = itemgetter('followers_count'), reverse = True)
x = y[0]
print("F.", x['screen_name'], 'has', x['followers_count'], 'followers')

filteredAcc = [a for a in accounts if a['verified'] == False]
y = sorted(filteredAcc, key = itemgetter('statuses_count'), reverse = True)
x = y[0]
print('G.', x['screen_name'],"has", x['statuses_count'], "tweets")

totes = 0
for a in accounts:
    totes += a['followers_count']
print('H.', round(totes / len(accounts)))

import statistics
new = []
for a in accounts:
	new.append(a['followers_count'])
print ('I.', statistics.median_low(new))