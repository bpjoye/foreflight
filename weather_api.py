import requests
import os
from dotenv import load_dotenv

load_dotenv()

# personal api key
API_KEY = os.environ.get('OPENWEATHERMAP_KEY')

# change city to search
city = "Charleston"

# api url
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}"

# parameters
params = {
    "appid": API_KEY,
    "units": 'imperial'
}

try:
    # send API request
    response = requests.get(url, params)
    response.raise_for_status()

    # format JSON
    weather_data = response.json()

    # extract information
    city_name = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    weather_description = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]

    # display data
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°F")
    print(f"Weather: {weather_description}")
    print(f"Wind Speed: {wind_speed} mph")

except requests.exceptions.RequestException as e:
    print(f"API Request Error: {e}")
except KeyError as e:
    print(f"Error: Missing expected data in the API response ({e})")
except Exception as e:
    print(f"An unexpected error occurred: {e}")