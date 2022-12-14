import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
count = int(input('Count: '))
position = int(input('Position: '))

while count > -1: #I put -1, not zero, because I need to print the user input web.
    html = urllib.request.urlopen(url, context=ctx).read() #opening and reading the input web
    soup = BeautifulSoup(html, 'html.parser') #Using BeautifulSoup for clena the html
    tags = soup('a') #extracting the anchor tag
    print('Retrieving:', url) #printing url. I put here the print() because i need to print the user input web.
    url = tags[position - 1].get('href', None) #Extracting only the url with .get('href', NONE) from the position - 1 in list tags.
    count -= 1
