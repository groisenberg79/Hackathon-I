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
    def create_wishlist(wishlist_name):
        '''create an empty wishlist (table) in database.'''
        cursor = connection.cursor()
        cursor.execute(f'''DROP TABLE IF EXISTS {wishlist_name}''')
        cursor.execute(f'''CREATE TABLE {wishlist_name} (
                                destination_id SERIAL PRIMARY KEY,
                                country_name VARCHAR(100),
                                city_name VARCHAR(100),
                                temp INT,
                                humidity INT)''')
        connection.commit()

    def table_exists(wishlist_name):
        '''check if wishlist wishlist_name exists in database;
        returns a boolean (True if it exists, False otherwise).'''
        cursor = connection.cursor()
        cursor.execute(
                        f'''SELECT EXISTS 
                            (
                                SELECT 1 
                                FROM pg_tables
                                WHERE schemaname = 'public'
                                AND tablename = '{wishlist_name}'
                            ) '''
                        )
        exists = cursor.fetchone()[0]
        connection.commit()
        return exists
    
    def row_exists(wishlist_name, country, city):
        cursor = connection.cursor()
        cursor.execute(f'''SELECT 
                                COUNT(*) FROM {wishlist_name}
                            WHERE 
                                {wishlist_name}.country_name = '{country}'
                                AND  {wishlist_name}.city_name = '{city}' ''')
        count = cursor.fetchall()
        cursor.close()
        if count[0][0] > 0:
            return 1
        else:
            return 0

    def add_to_wishlist(wishlist_name, place):
        cursor = connection.cursor()
        cursor.execute(f'''INSERT INTO 
                                {wishlist_name} (country_name, city_name, temp, humidity)
                            VALUES(
                                '{place.country_name}',
                                '{place.city_name}',
                                '{place.temp}',
                                '{place.humidity}')
                        ''')
        connection.commit()

    def delete_from_wishlist(wishlist_name, country, city):
        cursor = connection.cursor()
        cursor.execute(f'''DELETE FROM 
                            {wishlist_name}
                        WHERE
                            country_name = '{country}' AND
                            city_name = '{city}'
                        ''')
        connection.commit()

    
    def delete_wishlist(wishlist_name):
            cursor = connection.cursor()
            cursor.execute(f'''DROP TABLE  {wishlist_name} ''')
            connection.commit()

    def print_wishlist(wishlist_name):
            cursor = connection.cursor()
            cursor.execute(f'''SELECT
                                country_name, city_name, temp, humidity FROM {wishlist_name}
                        ''')
            rows = cursor.fetchall()
            destinations = ""
            for row in rows:
                destinations += f"-- COUNTRY: {row[0]} | CITY: {row[1]} | TEMP: {row[2]} Celsius | HUMIDITY: {row[3]}%\n"
            cursor.close()
            return destinations
    
    def print_names_wishlist():
        '''print the title  of all wishlists stored'''
        cursor = connection.cursor()
        cursor.execute('''SELECT
                            tablename FROM pg_tables
                        WHERE
                            schemaname = 'public' ''')
        t_list = cursor.fetchall()
        names_list = str()
        for elem in t_list:
            names_list += elem[0] + '\n'
        return names_list


# Wishlist.delete_wishlist('my_list')
# fake_place2 = Place('Barbenia', 'Convescus', -23, 34)
# Wishlist.delete_from_wishlist('my_list', fake_place2)
# table = Wishlist.print_wishlist('my_list')
# print(table)

# Wishlist.delete_wishlist('my_list2')
# Wishlist.delete_wishlist('my_list3')
# Wishlist.delete_wishlist('travel_destination')
# names = Wishlist.print_names_wishlist()
# print(names == "")
