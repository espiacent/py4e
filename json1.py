import urllib.request
import urllib.parse
import urllib.error
import json

list = []
url = 'http://py4e-data.dr-chuck.net/comments_1557542.json'

file = urllib.request.urlopen(url).read()

data = json.loads(file)

for person in data['comments']:
    list.append(person['count'])
