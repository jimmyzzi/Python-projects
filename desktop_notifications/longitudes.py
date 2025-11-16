import requests

def get_multiple_cities_coordinates(cities):
    coordinates = {}
    
    for city in cities:
        url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {"name": city, "count": 1}
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if data.get("results"):
                result = data["results"][0]
                coordinates[city] = {
                    "lat": result["latitude"],
                    "lon": result["longitude"]
                }
            else:
                coordinates[city] = None
                
        except requests.exceptions.RequestException:
            coordinates[city] = None
    
    return coordinates

# Example usage
if __name__ == "__main__":
    cities = ["London", "New York", "Tokyo", "Sydney", "Berlin"]
    
    print("Fetching coordinates for multiple cities...")
    results = get_multiple_cities_coordinates(cities)
    
    for city, coords in results.items():
        if coords:
            print(f"{city}: {coords['lat']:.4f}, {coords['lon']:.4f}")
        else:
            print(f"{city}: Not found")