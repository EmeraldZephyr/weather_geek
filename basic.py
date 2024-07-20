# Let's just send an http request to the national weather service API and print the response
# Let's also open the file and show the contents in a UI

import requests
import json
import tkinter as tk
import json

# This has to have special headers
headers = {
    'User-Agent':'myjweathermapp.app',
    'Accept': 'application/geo+json',
}

# Get coordinates from .env
file = open('location.env')
location_string = file.readline()

# URL to get the grid forecast by location
loc_url = f'https://api.weather.gov/points/{location_string}'

loc_request = requests.get(loc_url, headers=headers)

loc_dict = json.loads(loc_request.text)

office = loc_dict['properties']['cwa']
gridX = loc_dict['properties']['gridX']
gridY = loc_dict['properties']['gridY']

# This is the URL for the API
url = f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast'

# Send the request
response = requests.get(url, headers=headers)

# Write the response to a file
with open('response.json', 'w') as f:
    f.write(response.text)
    f.close()

