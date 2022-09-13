from django.shortcuts import render
from core.utils.endpoints import get_geo_data, search


def index(request):
    """Get data for data input for customer(location_in) or automatic search(location)"""
    
    data = []

    city = None

    while not city:
        response = get_geo_data()
        if response:
            city = response['city']

    qs = request.GET.get('key', None)
    location_in = request.GET.get('location_in', None)

    location = city

    context = {'city': city, 'search': False}

    if location_in:
        location = location_in

    if qs:
        data = search(keyword=qs, location=location)

        context = {
            'data': data,
            'city': location,
            'search': True
        }

    return render(request, 'core/index.html', context)
