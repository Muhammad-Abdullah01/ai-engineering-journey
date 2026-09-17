from weather import get_weather, WeatherError
from ai_summary import generate_weather_summary, AISummaryError


def display_weather(data: dict) -> None:
    print("\n" + "=" * 35)
    print(f"  Weather in {data['city'].title()}")
    print("=" * 35)
    print(f"  Condition:   {data['condition']}")
    print(f"  Temperature: {data['temperature_c']}°C")
    print(f"  Feels like:  {data['feels_like_c']}°C")
    print(f"  Humidity:    {data['humidity']}%")
    print("=" * 35)

    try:
        summary = generate_weather_summary(data)
        print(f"\n💬 {summary}\n")
    except AISummaryError as e:
        print(f"\n(AI summary unavailable: {e})\n")


def main():
    print("Weather CLI Tool")
    print("Type 'quit' to exit.\n")

    while True:
        city = input("Enter a city name: ").strip()

        if city.lower() == "quit":
            print("Goodbye!")
            break

        try:
            data = get_weather(city)
            display_weather(data)
        except WeatherError as e:
            print(f"\n⚠️  Error: {e}\n")


if __name__ == "__main__":
    main()