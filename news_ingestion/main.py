from fetcher.news_api_fetcher import fetch_news

articles = fetch_news()

print(len(articles))