from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

numlist = list()
tags = soup('span')
for tag in tags:
    numbers = tag.contents[0]
    integer = int(numbers)
    numlist.append(integer)
print(sum(numlist))