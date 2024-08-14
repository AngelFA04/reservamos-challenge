import requests
import os
from datetime import datetime


def get_weather_forecasting(lat: str, lon: str) -> list:
    """
    Get weather forecasting with the minimun and maximum temperature
    for the next 7 days

    Args:
        lat (str): Latitue
        lon (str): Longitude

    Returns:
        list: _description_
    """
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    exclude = "current,minutely,hourly"
    URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url=URL)
    except requests.exceptions.ConnectionError:
        raise Exception("There was an error in Openweather API")

    if response.status_code != 200:
        raise Exception("There was an error in Openweather API")

    # Get min and max temperature for the next 7 days
    daily_forecast_data= response.json()["daily"]

    daily_min_max_temps = []
    for day in daily_forecast_data:
        min_temp = day["temp"]["min"]
        max_temp = day["temp"]["max"]
        date = datetime.fromtimestamp(day["dt"]).strftime("%d-%m-%Y")
        daily_min_max_temps.append(
            {
                "date": date,
                "min_temp": min_temp,
                "max_temp": max_temp
            }
        )

    return daily_min_max_temps


def get_cities(name: str) -> list:
    """
    Get all the cities that match complete or partially with the name extracted
    from the Reservamos places API.

    Args:
        name (str): Name complete or partial of the city to search

    Returns:
        list: Cities data that match with the search name
    """
    URL = f"https://search.reservamos.mx/api/v2/places?q={name}"

    try:
        response = requests.get(url=URL)
    except requests.exceptions.ConnectionError:
        raise Exception("There was an error in Reservamos API request")

    if not response.status_code in [200, 201]:
        raise Exception("There was an error in Reservamos API request")

    # Filter the cities from the results
    cities = list(filter(lambda c: c["result_type"] == "city", response.json()))

    return cities
