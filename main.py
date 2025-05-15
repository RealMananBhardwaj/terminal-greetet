#!/usr/bin/env python3

import datetime
import os
import weather_info
import system_info



now = datetime.datetime.now()


hour = int(now.strftime("%H"))
if hour > 12:
    hour = hour%12

name = os.getlogin()
minute = int(now.strftime("%M"))
date = int(str.split(str(datetime.date.today()), "-")[2])
month = datetime.date.today().strftime("%B")
day = datetime.date.today().strftime("%A")
greeting = ""
greeter = ""
w_symbol = ""

if hour < 12:
    greeting = "Good morning"
    greeter = "🌄"
elif hour >= 12 and hour <= 5:
    greeting = "Good after noon"
    greeter = "☀️"
else:
    greeting = "Good evening"
    greeter = "🌙"

if weather_info.weather_description == "clear sky":
    w_symbol = "🌤️"
elif weather_info.weather_description == "few clouds":
    w_symbol = "🌥️"
elif weather_info.weather_description == "scattered clouds ":
    w_symbol = "☁️"
elif weather_info.weather_description == "broken clouds ":
    w_symbol = "🌫️"
elif weather_info.weather_description == "shower rain":
    w_symbol = "🌧️"
elif weather_info.weather_description == "rain":
    w_symbol = "🌦️"
elif weather_info.weather_description == "thunderstorm":
    w_symbol = "⛈️"
elif weather_info.weather_description == "snow":
    w_symbol = "❄️"
elif weather_info.weather_description == "mist":
    w_symbol = "💨"

os.system("echo ------------------------------------------ | lolcat -p 1.0")
os.system(f"echo {greeting}, {name.capitalize()}!   {greeter} {day}, {month}, {date} | lolcat -p 1.0")
os.system("echo ------------------------------------------ | lolcat -p 1.0")
print()
os.system(f"echo 📍 Location: Meerut, IN | lolcat -p 1.0")
os.system(f"echo {w_symbol}  Weather: {round(weather_info.temp, 2)}°C, {weather_info.weather_description.capitalize()} | lolcat -p 1.0")
print()
os.system(f"echo 🧠 Quote of your Life: | lolcat -p 1.0")
os.system(f'echo "  \'\'Wealth is what you don\'t see.\'\' - Some guy" | lolcat -p 1.0')
print()
os.system(f"echo 🖥️ System Info: | lolcat -p 1.0")
os.system(f"echo \"    {system_info.battery_usage}\" | lolcat -p 1.0")
os.system(f"echo \"    {system_info.ram_usage}\" | lolcat -p 1.0")
os.system(f"echo \"    {system_info.free_disk}\" | lolcat -p 1.0")
os.system("echo ------------------------------------------ | lolcat -p 1.0")