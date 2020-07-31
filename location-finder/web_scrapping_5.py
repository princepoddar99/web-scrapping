import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False :
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# enter the location as  a name like University of Nebraska
address = input('Enter location: ')

params={}
params['address'] = address
if api_key is not False:
    params['key'] = api_key
url = serviceurl + urllib.parse.urlencode(params)

print('Retrieving:', url)
uh = urllib.request.urlopen(url, context=ctx).read()
data=uh.decode()
print('Retrieved:', len(data), 'characters')

try:
    js = json.loads(data)
except :
    js = None

if not js or 'status' not in js or js['status'] != 'OK' :
    print('======== Failure ==========')
    print(data)

print(json.dumps(js, indent=4))

lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
location = js['results'][0]['formatted_address']
place = js['results'][0]['place_id']
print('Latitude:',lat)
print('Longitude',lng)
print('Location:',location)
print('Place id',place)