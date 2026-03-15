import requests

api_key = "0dc5fef2f07148819e7641ba49eb9b1b"

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=0dc5fef2f07148819e7641ba49eb9b1b"
    response = requests.get(url)
    data = response.json()
    return data["articles"]