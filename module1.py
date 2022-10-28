import urllib.parse, urllib.error, urllib.request
import xml.etree.ElementTree as ET
import ssl


url = 'http://py4e-data.dr-chuck.net/comments_1634468.xml'
sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read().decode()
tree = ET.fromstring(html)
#print(html)

for item in tree.findall('.//count'): # ".//" merge pana in count
    sum = sum + int(item.text)
print(sum)