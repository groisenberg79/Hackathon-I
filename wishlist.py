import psycopg2
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('HOSTNAME')
DB_NAME = os.getenv('DATABASE')
DB_USER = os.getenv('NAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_PORT = os.getenv('PORT')

# Create the PostgreSQL connection
connection = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

class Place:
    def __init__(self, country_name=None, city_name=None, temp=None, humidity=None):
        self.country_name = country_name
        self.city_name = city_name
        self.temp = temp
        self.humidity = humidity

class Wishlist:
    def create_wishlist():
        '''create an empty wishlist (table) in database.'''
        cursor = connection.cursor()
        cursor.execute('''DROP TABLE IF EXISTS wishlist''')
        cursor.execute('''CREATE TABLE wishlist (
                                destination_id SERIAL PRIMARY KEY,
                                country_name VARCHAR(100) NOT NULL,
                                city_name VARCHAR(100) NOT NULL,
                                temp INT NOT NULL,
                                humidity INT NOT NULL''')
        connection.commit()

    def add_to_wishlist(place):
        '''update wishlist with new entry (row) with data in Place object'''
        cursor = connection.cursor()
        cursor.execute(f'''INSERT INTO 
                                wishlist (country_name, city_name, temp, humidity)
                            VALUES(
                                {place.country_name},
                                {place.city_name},
                                {place.temp},
                                {place.humidity})
                        '''))
        connection.commit()

    def delete_from_wishlist(place):
        '''delete destination from wishlist.'''
        cursor = connection.cursor()
        cursor.execute(f'''DELETE FROM 
                            wishlist
                        WHERE
                            country_name = {place.country_name} AND
                            city_name = {place.city_name}
                        ''')
        connection.commit()

    def print_wishlist():
        '''print the wishlist.'''
        cursor = connection.cursor()
        cursor.execute('''SELECT
                            country_name, city_name, temp, humidity FROM wishlist
                       ''')
        rows = cursor.fetchall()
        destinations = ""
        for row in rows:
            destinations += f"-- CITY: {city_name} | COUNTRY: {country_name} | TEMP: {temp} Celsius | HUMIDITY: %{humidity}\n"
        cursor.close()
        return destinations