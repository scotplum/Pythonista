#Call Quotes API, retrieve keys and data for today's quote
#
import requests

url = 'http://quotes.rest/qod.json'
urljson = requests.get(url).json()
urldict = urljson['contents']
quotes = urldict['quotes']
quotes0 = quotes[0]
quotes_keys = quotes0.keys()
