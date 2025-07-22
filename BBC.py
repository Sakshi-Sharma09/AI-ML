import requests

from bs4 import BeautifulSoup

def fetch_news():

    url = "https://www.bbc.com/news"

    headers = {"User-Agent": "Mozilla/5.0"}

    

    req = requests.get(url, headers=headers)

    

    if req.status_code == 200:
        soup = BeautifulSoup(req.text, "html.parser")
        headlines = soup.find_all("h3")[:5]  # Get top 5 headlines
        print("Latest News Headlines:")
        for headline in headlines:
            print(headline.text)

        for i, headline in enumerate(headlines, 1):

            print(f"{i}. {headline.text.strip()}")

    else:

        print(f"Failed to fetch news. Status code: {req.status_code}")

# Example usage

fetch_news()