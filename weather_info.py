import requests

API_KEY = "Your-api-key"

city = "City,Country"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url).json()
temp = response['main']['temp'] - 273.15
weather = response['weather'][0]['main']
weather_description = response['weather'][0]['description']
