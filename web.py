# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count :"))
pos = int(input("Enter position :"))
check_count = 0
while True:
    check_count += 1
    check_pos = 0
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    #web crawling the page to fetch the last name
    tags = soup('a')
    for tag in tags:
        check_pos += 1
        if check_pos == pos:
            url=tag.get('href', None)
            if check_count == count:
                print(tag.text)
            break
    if check_count == count:
        break
