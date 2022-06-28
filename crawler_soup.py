import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input('Input URL:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
print(type(tags))
for tag in tags:
	print(tag.get('href', None))