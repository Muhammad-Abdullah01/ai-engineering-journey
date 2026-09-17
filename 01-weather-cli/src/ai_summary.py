import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class AISummaryError(Exception):
    """Raised when AI summary generation fails."""
    pass


def generate_weather_summary(weather_data: dict) -> str:
    prompt = (
        f"Here is current weather data for {weather_data['city']}:\n"
        f"- Temperature: {weather_data['temperature_c']}°C\n"
        f"- Feels like: {weather_data['feels_like_c']}°C\n"
        f"- Condition: {weather_data['condition']}\n"
        f"- Humidity: {weather_data['humidity']}%\n\n"
        f"Write a short, friendly, 1-2 sentence description of this "
        f"weather like you're texting a friend. No markdown, no lists."
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        raise AISummaryError(f"Could not generate AI summary: {e}")