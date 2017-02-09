#Call SuredBits API, retrieve keys and data for today's NBA games

import requests

url = 'http://api.suredbits.com/nba/v0/games'
urljson = requests.get(url).json()

nbagamestoday = urljson
nbagamestoday0 = nbagamestoday[0]
nbagamestoday_keys = nbagamestoday0.keys()
