import requests
from random import randint
from decouple import config
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.gis.geoip2 import geoip2


def search(keyword=None, location=None):
    headers = {'Authorization': 'Bearer ' + config('API_KEY')}

    if keyword and location:
        params = {'term': keyword, 'location': location}
    else:
        params = {'term': 'Restaurante', 'location': 'Goiânia'}

    result = requests.get(config('YELP_SEARCH_ENDPOINT'), headers=headers, params=params)

    print(result.json())
    
    return result.json()


    

def get_random_ip():
    return ".".join([str(randint(0, 255)) for i in range(4)])


def get_geo_data():
    geoip = GeoIP2()
    ip = get_random_ip()
    try:
        return geoip.city(ip)
    except geoip2.errors.AddressNotFoundError:
        return None
