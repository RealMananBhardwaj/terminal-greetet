import requests

API_KEY = "77b7ab70f60a75603ba34957918cf8d8"

city = "Meerut,IN"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url).json()
temp = response['main']['temp'] - 273.15
weather = response['weather'][0]['main']
weather_description = response['weather'][0]['description']