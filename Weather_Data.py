import requests

from bs4 import BeautifulSoup

def fetch_weather(city):

    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"

    headers = {"User-Agent": "Mozilla/5.0"}

    

    req = requests.get(url, headers=headers)

    

    if req.status_code == 200:

        soup = BeautifulSoup(req.text, "html.parser")

        weather = soup.find("span", class_="phrase").text

        print(f"Weather in {city.capitalize()}: {weather}")

    else:

        print(f"Failed to fetch weather for {city}. Status code: {req.status_code}")

# Example usage

fetch_weather("new-york")