import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def myfoo(intl_data):
    count = intl_data[1]
    return count

TotalJobs=0
intl_data_sorted = sorted(intl_data, key = myfoo, reverse=True)[:10]
for c in intl_data_sorted:
        print (str(c[0])+','+str(c[1]))
        TotalJobs+=int(c[1])
print("Other,%s" % (TotalJobs))
