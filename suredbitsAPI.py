import requests

nbagamestodayurl = 'http://api.suredbits.com/nba/v0/games'
nbagamestoday = requests.get(nbagamestodayurl).json()

nbagamestodaydict = {}
nbagamestodaydict = nbagamestoday[0]

#for di in nbagamestoday:
#    nbagamestodaydict[di['year']]={}
#    for k in di.keys():
#        if k =='year': continue
#        nbagamestodaydict[di['year']][k]=di[k]



nbagamestoday_keys = nbagamestodaydict.keys()

print(nbagamestoday_keys)

#print(nbagamestoday)
#print(nbagamestoday_keys)
