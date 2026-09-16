from weather import get_weather, WeatherError

def display_weather(data : dict) -> None:
    print("\n" + "=" * 35)
    print(f"Weather in {data['city'].title()}")
    print("=" *35)
    print(f"Condition: {data['condition']}")
    print(f"Temperature: {data['temperature_c']}°C")
    print(f"  Feels like:  {data['feels_like_c']}°C")
    print(f"  Humidity:    {data['humidity']}%")
    print("=" * 35 + "\n")

def main():
    print("Weather CLI Tool")
    print("Type 'quit' to exit.\n")

    while True:
        city = input("Enter a city name: ").strip()

        if city.lower() == 'quit':
            print("Good Bye")
            break

        try:
            data = get_weather(city)
            display_weather(data)
        except WeatherError as e:
            print(f"\n Error: {e}\n")


if __name__ == "__main__":
    main()
