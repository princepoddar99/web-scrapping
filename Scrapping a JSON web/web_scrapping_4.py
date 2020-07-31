import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url:')
html = urllib.request.urlopen(url, context=ctx).read()

try:
    info = json.loads(html)
except :
    print("None")

sum=0
comments = info['comments']
for count in comments:
    sum = sum + count['count']

print (sum)