import requests
import time
from datetime import datetime, timedelta
from datetime import date



# API endpoint and key
API_URL = "https://newsapi.org/v2/everything"
API_KEY = "e10fed0319c54ba7ad9cefade9a3200c"

# Source of data: https://newsapi.org/

current_date = date.today() - timedelta(days=1)

# Query parameters
params = {
    'q': 'tesla',
    'from': current_date,
    'sortBy': 'publishedAt',
    'apiKey': API_KEY
}

def fetch_latest_articles():
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])

        print(f"\nFetched {len(articles)} articles at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for article in articles[:5]:  # Show only top 5
            print(f"Title: {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"Published At: {article['publishedAt']}")
            print(f"URL: {article['url']}\n")
    except Exception as e:
        print(f"Error fetching data: {e}")

# Simulate live stream: fetch every 60 seconds.
if __name__ == "__main__":
    while True:
        fetch_latest_articles()
        time.sleep(60)  # Wait 1 minute before fetching again
