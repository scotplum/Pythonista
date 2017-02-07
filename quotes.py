#Call Quotes API, retrieve keys and data for today's quote
#
import requests

url = 'http://quotes.rest/qod.json'
urlquotes = requests.get(url).json()
