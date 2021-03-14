import json
from 'C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\my_notebooks\\.modules' import api_keys
import requests


url = "http://api.openweathermap.org/data/2.5/forecast"
query = {'q': 'Copenhagen,dk',
         'mode': 'json',
         'units': 'metric',
         'appid': api_keys.OPENWEATHERMAP_KEY}
r = requests.get(url, params=query)

r.json()