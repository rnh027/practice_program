from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#tested url :'http://python-data.dr-chuck.net/comments_42.html','http://py4e-data.dr-chuck.net/comments_724704.html'
url = input("Enter -")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")
data = soup.findAll("span", { "class":"comments" })
numbers = list(map(int,[d.text for d in data]))
print(sum(numbers))
