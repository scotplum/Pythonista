#Call Eventful API, retrieve JSON and parse into usable data
#Example Call: 
#http://api.eventful.com/rest/events/search?...&where=32.746682,-117.162741&within=25

import requests
import time

secret = '&app_key=3K9J8pCvC5gSwNw7'
url = 'http://api.eventful.com/json/events/search?...&where=35.6131551,-97.6385368&within=25' + secret

call = requests.get(url).json()
events = call['events']
event = events['event']

callkeys = call.keys()

#for i in event:
	#print (i['url'], i['venue_name'])

#print(call)
#print(event)

