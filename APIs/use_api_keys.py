import requests

base_url = "https://openweathermap.org/data/2.5/forecast"

parameters = {
    "q": "Paris,FR",
    "appid": "hidden"
}

response = requests.get(base_url, params=parameters)

print(response.text)