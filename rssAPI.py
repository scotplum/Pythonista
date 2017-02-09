import feedparser

url = 'http://feeds.feedburner.com/TheWirecutter'
url_parsed = feedparser.parse(url)

feed_title = url_parsed.feed.title
feed_description =  url_parsed.feed.description
item_0_title = url_parsed.entries[0].title
