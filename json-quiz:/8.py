import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'
data = json.loads(requests.get(data_url).text)
books = data['results']['books']

x = 0
for item in books:
	if item['publisher'] == "Scribner":
		x += 1
print("A.", x)

x = 0
keyword = "detective"
for item in books:
	if keyword in item['description'].lower():
		x += 1
print("B.", x)

from operator import itemgetter
y = sorted(books, key = itemgetter('weeks_on_list'), reverse = True)
x = y[0]
s = "|".join([x['title'], str(x['weeks_on_list'])])
print("C.", s)

y = sorted(books, key = itemgetter('rank_last_week'), reverse = True)
x = y[0]
s = "|".join([x['title'], str(x['rank']), str(x['rank_last_week'])])
print("D.", s)

x = 0
for item in books:
    if item['rank_last_week'] == 0:
        x += 1
print("E.", x)

filteredBooks = [item for item in books if item['rank_last_week'] == 0]
y = sorted(filteredBooks, key = itemgetter('rank'))
x = y[0]
s = "|".join([x['title'], str(x['rank'])])
print('F.', s)

def calc_rank_change(book_obj):
    return book_obj["rank_last_week"] - book_obj["rank"]
books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]
x = max(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("G.", s)

x = min(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("H.", s)

changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for v in changes if v > 0]
s = sum(x)
print("I.", s)

x = [v for v in changes if v < 0]
s = "|".join([str(len(x)), str(sum(x))])
print("J.", s)

print('K.', max([len(b['title']) for b in books]))

totes = 0
for b in books:
    totes += len(b['title'])
print('H.', round(totes / len(books)))
