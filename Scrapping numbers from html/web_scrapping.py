import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url:')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

sum=0.0
count=0
tags=soup('span')
for tag in tags :
    sum = sum+float(tag.contents[0])
    count = count+1
print("Count",count)
print("Sum",sum)