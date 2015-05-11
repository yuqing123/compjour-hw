import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def myfoo(intl_data):
    count = intl_data[1]
    return count

intl_data_sorted = sorted(intl_data, key = myfoo, reverse=True)
for c in intl_data_sorted:
    if c[1] > 10:
        print (str(c[0])+','+str(c[1]))