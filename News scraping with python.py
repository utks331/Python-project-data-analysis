#Automatic News Scraping with Python, Newspaper and Feedparser

#1. Import the required modules newspaper, and feedparser.
import newspaper
import feedparser

#2. We define a function called scrape_news_from_feed(),
# which takes a feed URL as input.Inside the function, we first parse the RSS feed using the feedparser.parse() method.
# This returns a dictionary containing various information about the feed and its entries.
def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        article = newspaper.Article(entry.link)
        #download and parse the article
        article.download()
        article.parse()
        #Extracting relevant information
        articles.append({
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text
        })
    return articles

feed_url = 'http://feeds.bbci.co.uk/news/rss.xml'
articles = scrape_news_from_feed(feed_url)

for article in articles:
    print('Title:', article['title'])
    print('Author:', article['author'])
    print('Publish Date:', article['publish_date'])
    print('Content:', article['content'])
    print()


