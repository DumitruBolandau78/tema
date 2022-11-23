import requests
import json

API_KEY = "aafda7022737abd3d9051eb4e7b64fad"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city = input('Introdu numele orasului:')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
rasp = requests.get(request_url)
data = json.loads(rasp.text)
print(data)