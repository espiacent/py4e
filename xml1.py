import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET


list = []

url = 'http://py4e-data.dr-chuck.net/comments_1557541.xml'

file = urllib.request.urlopen(url).read()

tree = ET.fromstring(file)

results = tree.findall('comments/comment')
data_len = len(results)

for result in results:
    number = float(result.find('count').text)
    list.append(number)

total = sum(list)
print(total)
