#import requests
#BASE_USAJOBS_URL = "https://inventory.data.gov/api/action/datastore_search"
#dataset = 'b626ef1f-9019-41c4-91aa-5ae3f7457328'
#atts = {"resource_id ": dataset}
#resp = requests.get(BASE_USAJOBS_URL, params = atts)
#data = resp.json()
#print(data)

import requests
import json
url = 'https://inventory.data.gov/api/action/datastore_search?resource_id=b626ef1f-9019-41c4-91aa-5ae3f7457328'
data = json.loads(requests.get(url).text)
print(data['result']['total'])