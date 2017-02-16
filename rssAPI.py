import feedparser

url = 'http://feeds.feedburner.com/TheWirecutter'
url_parsed = feedparser.parse(url)
url_entries = url_parsed.entries
url_entries_selection = url_entries[0:5]
#url_titles = url_parsed.entries.title


feed_title = url_parsed.feed.title
feed_description =  url_parsed.feed.description
item_0_title = url_parsed.entries[0].title

rsstitles = []
rsslinks = []

#Select all titles and add to rsstitles list
for i in url_entries_selection:
	rsstitles.append(i['title'])

#Select all links and add to rsslinks
for i in url_entries_selection:
	rsslinks.append(i['link'])

print(feed_title)
#Print Titles: Links
for i in url_entries_selection:
	print("[" + i['title'] + "] (" + i['link'] + ")")

#example of selecting a range of titles and assigning to list name
#for i in url_entries[0:3]:
#    rssrangetitles.append(i['title']) 



