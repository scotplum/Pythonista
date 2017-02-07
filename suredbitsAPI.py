#Call SuredBits API, retrieve keys and data for today's NBA/NFL games
#
import requests

nbagamestodayurl = 'http://api.suredbits.com/nba/v0/games'
nbagamestoday = requests.get(nbagamestodayurl).json()
nflgamestodayurl = 'http://api.suredbits.com/nfl/v0/games'
nflgamestoday = requests.get(nflgamestodayurl).json()

nbagamestodaydict = {}
nbagamestodaydict = nbagamestoday[0]
nbagamestoday_keys = nbagamestodaydict.keys()

nflgamestodaydict = {}
nflgamestodaydict = nflgamestoday[0]
nflgamestoday_keys = nflgamestodaydict.keys()


print(nbagamestoday_keys)
print(nflgamestoday_keys)
