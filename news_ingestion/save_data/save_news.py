import json

def save_articles(articles):
    with open("articles.json", "w") as file:
        json.dump(articles, file, indent=4)