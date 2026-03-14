import requests
import json

API_Key = "0dc5fef2f07148819e7641ba49eb9b1b"

url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=0dc5fef2f07148819e7641ba49eb9b1b"

response = requests.get(url)

data = response.json()

print(data)

articles = data["articles"]

for article in articles:
    title = article["title"]
    url = article["url"]
    published = article["publishedAt"]

print(title, url, published)

with open("aticles.json", "w") as file:
    json.dump(articles, file, indent=4)