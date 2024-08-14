from django.http import JsonResponse

from utils import get_cities, get_weather_forecasting


def forecast_city_weather_view(request):
    city_name = request.GET.get("city_name")

    if not city_name:
        return JsonResponse({
            "error": "'city_name' parameter is required"
        })

    # Search city name
    cities = get_cities(city_name)

    # Dictionary to store the cities for the response
    cities_response = []
    # Get the temperature for all the cities
    for city in cities:
        lat = city["lat"]
        long = city["long"]

        forecast = get_weather_forecasting(lat, long)
        city_name = city["city_name"]
        
        cities_response.append({
            "city_name": city_name,
            "next_week_temperatures": forecast
        })
    
    return JsonResponse(
        {"response": cities_response}
    )

