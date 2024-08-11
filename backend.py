# coding=utf-8
# we need: dates, how many days, temperatures, place
from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta

load_dotenv()
API_key = os.getenv('OWMAPIZH')

if API_key:
    print("API Key retrieved successfully.")
else:
    print("API Key not found.")


def get_data(place, forecast_days, kind):
    dates = []
    temperatures = []
    icons = []
    data, lon, lat = find_city(place)
    weather_data = find_weather(lon, lat)
    today = datetime.now().date()
    end_date = today + timedelta(days=forecast_days)

    for i in weather_data['list']:
        date = datetime.strptime(i['dt_txt'], "%Y-%m-%d %H:%M:%S")
        entry_date = date.date()
        if today <= entry_date <= end_date:
            dates.append(date)
            temperatures.append(i['main']['temp'])
            icons.append(i['weather'][0]['icon'])
    return dates, temperatures, icons


def find_city(city_name):
    city_loc = (
        f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}"
        f"&appid={API_key}")
    response = requests.get(city_loc)
    if response.status_code == 200:
        # Request was successful
        data = response.json()  # Parse the JSON response
        lon = data[0]['lon']
        lat = data[0]['lat']
        data = "CityOK"
    else:
        # Handle errors
        data = f"Error: {response.status_code} - {response.text}"
        lon = lat = ""
    return data, lon, lat


def find_weather(lon, lat):
    weather = (f"https://api.openweathermap.org/data/2.5/"
               f"forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric")
    response = requests.get(weather)
    if response.status_code == 200:
        # Request was successful
        data = response.json()  # Parse the JSON response

    else:
        # Handle errors
        data = f"Error: {response.status_code} - {response.text}"
    return data
