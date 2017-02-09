#Call Quotes API, retrieve keys and data for today's quote
#
import requests

url = 'http://quotes.rest/qod.json'
urljson = requests.get(url).json()
urlcontents = urljson['contents']
urlquotes = urlcontents['quotes']
url0 = urlquotes[0]
urldict = url0.keys()
