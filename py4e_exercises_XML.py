import urllib.request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1633420.xml'
sum_list= []

data = urllib.request.urlopen(url).read()
print('Retrieving: http://py4e-data.dr-chuck.net/comments_1633420.xml')
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
comments = tree.findall('comments/comment')
print('Count:', len(comments))

for line in comments:
    x = line.find('count').text
    y = int(x)
    sum_list.append(y)
print('Sum:', sum(sum_list))