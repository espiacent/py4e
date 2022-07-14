from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fout = open('fout.txt', 'w')
lst = []
t_lst = []

url = input('Enter - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1557539.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents)
    # print('Attrs:', tag.attrs)
    fout.write(str(tag.contents))
    lst.extend(tag.contents)

try:
    lst = list(map(int, lst))
    print(round(sum(lst)))
except:
    print('Something went wrong.')
    raise SystemExit
