 if "current_weather" in weather_res:
        # Extract temperature and wind speed
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]
        
        # Format the weather information
        weather_info = f"{city}: {temp}°C, Wind {wind} km/h"
        print("Weather:", weather_info)
        
        # Show desktop notification
        toaster.show_toast(
            "Weather Update",
            weather_info,
            duration=5
        )