#Call Dark Sky API, retrieve JSON and parse into usable data
#
import requests
import json
import time

secret = '0202c0488245dc09210780756c9fb133'
url = 'https://api.darksky.net/forecast/' + secret + '/' + '35.6131551' + ',' + '-97.6385368'

call = requests.get(url).json()
currently = call['currently']
timecurrently = int(currently['time'])
tempcurrently = str(currently['temperature'])
summarycurrently = currently['summary']
hourly = call['hourly']
datahourly = hourly['data']
datahourly0 = datahourly[0]

#for v in currently.items():
#	print(v)

currenttimeout = time.strftime('%H:%M:%S', time.localtime(timecurrently))
currentout = 'As of ' + currenttimeout + ' local time, the temperature is ' + tempcurrently + ' degrees Fahrenheit and the outlook is ' + summarycurrently.lower() +'.'

print(currentout)
print(datahourly0)
for i in datahourly:
	print (i['temperature'], + i['cloudCover'])

