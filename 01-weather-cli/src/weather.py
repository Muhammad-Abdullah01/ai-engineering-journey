import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


class WeatherError(Exception):
    """Custom exception for weather-related failures."""
    pass


def get_weather(city: str) -> dict:
    if not city or not city.strip():
        raise WeatherError("City name cannot be empty.")

    if not API_KEY:
        raise WeatherError("API key not found. Check your .env file.")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # so we get Celsius directly
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise WeatherError("Request timed out. Check your internet connection.")
    except requests.exceptions.ConnectionError:
        raise WeatherError("Could not connect. Check your internet connection.")
    except requests.exceptions.HTTPError:
        raise WeatherError(
        f"Could not find weather data for '{city}'. "
        f"Status code: {response.status_code}. "
        f"Response: {response.text}"
        )

    try:
        data = response.json()
        return {
            "city": city,
            "temperature_c": data["main"]["temp"],
            "feels_like_c": data["main"]["feels_like"],
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
        }
    except (KeyError, IndexError, ValueError):
        raise WeatherError("Unexpected response format from weather service.")