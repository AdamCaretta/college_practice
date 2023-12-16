'''import requests
import json

# x = requests.get('https://swapi.dev/api/starships/')
# print(json.dumps(x.json(), indent=4, sort_keys=True))

import time

past_time = int(time.time() - (4 * 24 * 60 * 60))
# params = {'lat':53, 'lon':27.5, 'dt':past_time, 'units':'imperial', 'appid':}
x = requests.get(
    "http://api.openweathermap.org/data/2.5/onecall/timemachine", params=params
)
print(x.url)
print(x.status_code)
print(json.dumps(x.json(), indent=4, sort_keys=True))
'''