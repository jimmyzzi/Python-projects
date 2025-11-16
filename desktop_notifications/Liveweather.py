import requests
from win10toast import ToastNotifier

toaster = ToastNotifier()

city = "Kilifi"
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}
geo_res = requests.get(geo_url, params=geo_params).json()

if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {  # Fixed the variable name
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    weather_res = requests.get(weather_url, params=weather_params).json()  # Now this matches
    print(weather_res)
    if "current_weather" in weather_res:
        temp = weather_res["current_weather"]["temperature"]  # Fixed typo: "cureent_weather" to "current_weather"
        wind = weather_res["current_weather"]["windspeed"]
        weather_info = f"{city}: {temp}°C, Wind {wind} km/h"
        print("Weather:", weather_info)
        toaster.show_toast(  # Fixed: using 'toaster' instead of 'notification'
            "Weather Update",
            weather_info,
            duration=5  # Fixed: 'timeout' should be 'duration' for win10toast
        )
    else:
        print("Weather data not found")
else:
    print("City not found")