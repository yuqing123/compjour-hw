import requests
import json
url = 'https://api.github.com/users/18f'
data = json.loads(requests.get(url).text)
print(data['public_repos'])