# ==========================================
# Task 2 - API Integration & JSON Parsing
# Weather Information App
# ==========================================

import requests
import json

try:
    # Input city name
    city = input("Enter city name: ")

    # API URL (free weather API)
    url = f"https://wttr.in/{city}?format=j1"

    # Fetch data from API
    response = requests.get(url, timeout=10)

    # Check response status
    if response.status_code == 200:

        data = response.json()

        current = data["current_condition"][0]

        # Weather information dictionary
        weather_info = {
            "City": city,
            "Temperature_C": current["temp_C"],
            "FeelsLike_C": current["FeelsLikeC"],
            "Humidity": current["humidity"],
            "Weather": current["weatherDesc"][0]["value"],
            "WindSpeed_Kmph": current["windspeedKmph"]
        }

        print("\n===== WEATHER REPORT =====")

        for key, value in weather_info.items():
            print(f"{key}: {value}")

        # Simple filter logic (enhancement)
        if int(current["temp_C"]) > 30:
            print("\n🌡️ It is a hot day!")
        else:
            print("\n🌤️ Weather is moderate/cool.")

        # Save to JSON file
        with open("city_weather.json", "w") as file:
            json.dump(weather_info, file, indent=4)

        print("\nWeather data saved to city_weather.json")

    else:
        print("API Error:", response.status_code)

except requests.exceptions.ConnectionError:
    print("Internet connection error.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except Exception as e:
    print("Unexpected Error:", e)
    