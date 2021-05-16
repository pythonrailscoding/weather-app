from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if city:
            res = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ab2e79c1529dff9433f9dbe2e310cc1e").read()
            json_data = json.loads(res)
            data = {
                "city_name": str(json_data["name"]),
                "country_code": str(json_data['sys']['country']),
                "coordinates": str(json_data['coord']['lon']) + ' degree Longitude and ' + str(json_data['coord']['lat']) + ' degree Latitude',
                "temp": str(json_data['main']['temp']),
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
                "description": json_data["weather"][0]["main"],
                "icon": "http://openweathermap.org/img/w/"+json_data["weather"][0]["icon"]+".png",
                }
            
            return render(request, 'index.html', {'data':data, 'city':city})
        else:
            data = ''
            return render(request, 'index.html', {'data':data})
    else:
        return render(request, 'index.html', {})
