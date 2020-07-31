import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE


url = input('Enter the url:')
c=input('Enter the count:')
count=int(c)
p=input('Enter the position:')
pos=int(p)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print("Retrieving: ",url)

names=[]

for i in range(count) :
    tags = soup('a')

    #get to the tag of the correct position
    tag = tags[pos-1]

    # extract the name of the tag which includes the initial name also
    n = str(tag.contents[0])
    names.append(n)

    #extract the url of the tag and move to the new page
    url=str(tag.get('href',None))
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

print(names)