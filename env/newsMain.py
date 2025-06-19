import feedparser
from newspaper import Article
from datetime import datetime
import ssl

# RSS feed URL for TOI Top Stories
RSS_FEED_URL = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"

# Optional: Bypass SSL verification issues
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def summarize_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()

        # Parse text and extract first 2 sentences
        article_text = article.text.strip().replace('\n', ' ')
        sentences = article_text.split('.')
        if len(sentences) >= 2:
            summary = '. '.join(sentences[:2]).strip() + '.'
        else:
            summary = article_text.strip()

        return summary
    except Exception as e:
        return f"⚠️ Could not summarize article: {e}"

# fetch_toi_news
def fetch_toi_news():
    print(f"\n📰 Times of India - Top Stories ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
    
    feed = feedparser.parse(RSS_FEED_URL)

    if not feed.entries:
        print("⚠️ No news items found.")
        return

    for i, entry in enumerate(feed.entries[:5], start=1):  # Limit to top 5
        print(f"{i}. {entry.title}")
        print(f"   Published: {entry.published}")
        print(f"   Link: {entry.link}")
        
        summary = summarize_article(entry.link)
        print(f"   Summary: {summary}\n")

if __name__ == "__main__":
    fetch_toi_news()
