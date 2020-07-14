import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#read urlof xml data from web read file by using urllib parse and extract count finally sum


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#enter the url of xml file
address = input('Enter location: ')
parms = dict()
parms['address'] = address
url = urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#decode the exteracted url which convert in to string
tree = ET.fromstring(data.decode())

results = tree.findall('comments/comment')
#total count of available files
print("Count:",len(results))
sum = 0
for cnt in results:
    sum +=int(cnt.find('count').text)
print("Sum:",sum)
