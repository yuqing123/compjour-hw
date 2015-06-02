from lxml import html
import requests
page = requests.get('http://www.fda.gov/NewsEvents/MeetingsConferencesWorkshops/PastMeetingsWithFDAOfficials/ucm439318.htm')
tree = html.fromstring(page.text)
result = tree.xpath('//article/h4/text()')
print (len(result))