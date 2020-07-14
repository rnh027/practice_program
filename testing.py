import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
parms = dict()
parms['address'] = address
url = urllib.parse.urlencode(address)
print('Retrieving', url)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data.decode())

results = tree.findall('comments/comment')
print("count:",len(results))
sum = 0
for i in results:
    sum +=int(i.find('count').text)
print(sum)
