import requests

zip = '73142'
url = 'https://congress.api.sunlightfoundation.com/legislators/locate?zip=' + zip
urljson = requests.get(url).json()
sunlight = urljson['results']
sunlight0 = sunlight[0]
sunlight_keys = sunlight0.keys()
