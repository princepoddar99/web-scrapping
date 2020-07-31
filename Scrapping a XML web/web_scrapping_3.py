import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
html = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(html)
print("Retrieving:",url)

comments = tree.findall('comments/comment')
total = 0.0
count=0
for comment in comments :
    total = total + float(comment.find('count').text)
    count = count + 1
print("Count:",count)
print("Sum:",total)

