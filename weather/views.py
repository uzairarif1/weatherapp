from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=d3b6a62b5a2b0cf86809347d2ea9242f').read()
        json_data = json.loads(res)

        country_code = json_data['city']['country']
        coordinates = str(json_data['city']['coord']['lon']) + ' ' + str(json_data['city']['coord']['lat'])
        population = json_data['city']['population']
        # Extract weather data for the first forecast entry (index 0)
        first_forecast = json_data['list'][0]
        temp = str(first_forecast['main']['temp']) + 'K'  # Temperature in Kelvin
        pressure = first_forecast['main']['pressure']
        humidity = first_forecast['main']['humidity']

        data = {
            "country_code": country_code,
            "coordinate": coordinates,
            "temp": temp,
            "pressure": pressure,
            "humidity": humidity,
            "population": population
        }
    else:
        city=''
        data={}
    return render(request, 'index.html',{'city':city,'data':data})


# data = {
#             "country_code": str(json_data['cnt']),
#             "coordinate": str(json_data['city']['coord']['lon']) + ' ' +
#             str(json_data['city']['coord']['lat']),
            
#             "temp": str(json_data['main']['temp'])+'k',
#             "pressure": str(json_data['main']['pressure']),
#             "humidity": str(json_data['main']['humidity']),
#         }