# import requests  # type: ignore
# from dotenv import load_dotenv
# import os
# from pprint import pprint
#
# load_dotenv()
#
# def get_current_weather():
#   print('\n Get the current weather conditions \n')
#
#   city = input(" enter the city name: ")
#
#   request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
#
#   weather_data = requests.get(request_url).json()
#
#   pprint(weather_data)
#
# get_current_weather()

import requests  # type: ignore
from dotenv import load_dotenv
import os

load_dotenv()


def get_current_weather():
  print('\n🌤️  Get the current weather conditions\n')

  city = input("Enter the city name: ")

  request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

  response = requests.get(request_url)
  weather_data = response.json()

  if weather_data.get("cod") != 200:
    print(f"\n❌ Error: {weather_data.get('message', 'Unable to fetch weather')}")
    return

  # Extracting relevant data
  city_name = weather_data['name']
  country = weather_data['sys']['country']
  temp = weather_data['main']['temp']
  feels_like = weather_data['main']['feels_like']
  weather_main = weather_data['weather'][0]['main']
  weather_desc = weather_data['weather'][0]['description']
  humidity = weather_data['main']['humidity']
  pressure = weather_data['main']['pressure']
  wind_speed = weather_data['wind']['speed']
  wind_deg = weather_data['wind']['deg']
  cloudiness = weather_data['clouds']['all']
  visibility = weather_data['visibility'] / 1000  # Convert to km

  print(f"\n📍 Weather Report for {city_name}, {country}")
  print(f"🌡️  Temperature      : {temp}°C (Feels like {feels_like}°C)")
  print(f"☁️  Condition        : {weather_main} ({weather_desc.capitalize()})")
  print(f"💧 Humidity         : {humidity}%")
  print(f"🌬️  Wind            : {wind_speed} m/s at {wind_deg}°")
  print(f"🔵 Pressure         : {pressure} hPa")
  print(f"🌫️  Visibility       : {visibility} km")
  print(f"☁️  Cloud Cover     : {cloudiness}%")


get_current_weather()
