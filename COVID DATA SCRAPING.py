import requests
from bs4 import BeautifulSoup

def fetch_covid_data(country):
    # Format the country name for the URL
    url = f"https://www.worldometers.info/coronavirus/country111/{country.lower()}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    print (req)
    if req.status_code == 200:

        # print(req.text)

        bsObj = BeautifulSoup(req.text, "html.parser")
        data = bsObj.find_all("div", class_="maincounter-number")
        #data_close = bsObj.find_all("div", class_="number-table-main")
        
        # Ensure data has the expected elements
        if len(data) >= 3:
            print(f"COVID-19 Data for {country.capitalize()}:")
            print("Total Cases:", data[0].text.strip())
            print("Total Deaths:", data[1].text.strip())
            print("Total Recovered:", data[2].text.strip())
            #print("Closed Cases:", data_close[0].text.strip())
            print("-" * 40)
        else:
            print(f"Error: Couldn't find all required data for {country.capitalize()} on the webpage.")
    else:
        print(f"Failed to fetch the page for {country.capitalize()}. Status code: {req.status_code}")

# List of countries you want to fetch data for
countries = ["us", "india", "china", "brazil", "russia" , "bhuyvf"]

# Fetch data for each country
for country in countries:
    fetch_covid_data(country)
