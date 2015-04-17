import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/single-tweet-librarycongress.json'
data = json.loads(requests.get(data_url).text)

print('A.', data['created_at'])
print('B.', data['user']['created_at'])
print('C.', data['text'])
print('D.', data['user']['screen_name'])
print('C.', data['id'])
print('F.', data['entities']['user_mentions'])
hashtag_objs = data['entities']['hashtags']
hashtag_texts = []
for h in hashtag_objs:
    hashtag_texts.append(h['text'])
print('G.', ','.join(hashtag_texts))

urls_objs = data['entities']['urls']
urls_new = []
for i in urls_objs:
    urls_new.append(i['display_url'])
print('F.', ','.join(urls_new))