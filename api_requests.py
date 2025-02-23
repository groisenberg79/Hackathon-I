import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_LOC = os.getenv('API_KEY_LOC')

def kelvin_to_celsius(kelvin):
        """Convert temperature from Kelvin to Celsius."""
        celsius = kelvin - 273.15
        return int(celsius)

class ApiRequest:
    def request_loc_code(country_name):
        '''take a country name and return its ISO code.
        String --> String'''
        response = requests.get(f"https://iso3166-2-api.vercel.app/api/country_name/{country_name}")
        data = response.json()
        json_string = json.dumps(data)
        json_dict = json.loads(json_string)
        return list(json_dict.keys())[0] # have to check for 200, 400 cases

    def request_loc(city_name, country_code):
        '''take a city name and a country code (strings) and returns
        a tuple with the latitude and longitude of the city.
        (String, String) --> (Int, Int)'''
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}%2c{country_code}&limit=1&appid={API_KEY_LOC}")
        data = response.json()
        json_string = json.dumps(data)
        json_dict = json.loads(json_string)
        lat_lon = (int(json_dict[0]['lat']), int(json_dict[0]['lon'])) # have to check for 200, 400 cases
        return lat_lon

    def request_temp_hum(lat, lon):
        '''takes latitude and longitude of a city and returns
        current temperature (Celsius) and humidity (percentage).
        (Int, Int) --> (Int, Int)'''
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?&lat={int(lat)}&lon={int(lon)}&appid={API_KEY_LOC}")
        data = response.json()
        json_string = json.dumps(data)
        json_dict = json.loads(json_string)
        return (kelvin_to_celsius(json_dict['list'][0]['main']['temp']),
                json_dict['list'][0]['main']['humidity'])


# country = request_loc_code('france')
# print(country)

# lat_lon = request_loc('paris', 'FR')
# print(lat_lon)