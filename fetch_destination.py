import psycopg2
import requests
import json
import random
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

cursor = connection.cursor()
cursor.execute('''DROP TABLE IF EXISTS travel_destination''')
cursor.execute('''CREATE TABLE travel_destination (
                        destination_id SERIAL PRIMARY KEY,
                        country_name VARCHAR(100) NOT NULL,
                        city_name VARCHAR(100) NOT NULL,
                        date_of_travel DATE NOT NULL,
                        av_temp INT NOT NULL,
                        pop_size INT NOT NULL)''')