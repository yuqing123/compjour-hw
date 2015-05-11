import json
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())

domestic_data_sorted = sorted(domestic_data)
for s in domestic_data_sorted:
    if s[1] < 100:
        print (str(s[0])+','+str(s[1]))