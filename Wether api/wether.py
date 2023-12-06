
# https://openweathermap.org/api
# to run:   python wether.py

import requests

API_KEY = "0876877951e36f7aed4426f8a362b06c"
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input("Enter city name: ")
requet_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requet_url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp']-273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "Celsius")

else:
    print("Error in the HTTP request")
