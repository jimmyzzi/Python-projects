import requests

def fetch_weather_data(lat, lon):
    # Open-Meteo API endpoint for current weather
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m,wind_direction_10m&timezone=auto"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Extract current weather data
        current = data['current']
        return {
            'temperature': current['temperature_2m'],
            'humidity': current['relative_humidity_2m'],
            'weather_code': current['weather_code'],
            'wind_speed': current['wind_speed_10m'],
            'wind_direction': current['wind_direction_10m'],
            'time': current['time']
        }
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None