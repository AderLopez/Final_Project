#import url lib and json libraries:
import urllib.request
import json

#Using a country name we can get the information of that country:
def country(name):
    print(name)
    url = f"https://restcountries.com/v3.1/alpha?codes={name}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    return result