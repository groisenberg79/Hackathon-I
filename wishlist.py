import db_config

# url = 'https://api.geoapify.com/v2/places?categories=catering.restaurant,catering.cafe&filter=place:51d9e66b3b1264414059e7edbe19eb0a4040f00101f9015e18150000000000c00208&apiKey=06be9c16bc6d400d95a00bb9933f4e84'

# response = requests.get(url)
# data = response.json()
# json_string = json.dumps(data, indent=2)
# print(json_string) 

class Wishlist:

    def create_wishlist():
        cursor = connection.cursor()
        cursor.execute('''DROP TABLE IF EXISTS travel_destination''')
        cursor.execute('''CREATE TABLE travel_destination (
                                destination_id SERIAL PRIMARY KEY,
                                country_name VARCHAR(100) NOT NULL,
                                city_name VARCHAR(100) NOT NULL,
                                date_of_travel DATE NOT NULL,
                                av_temp INT NOT NULL,
                                pop_size INT NOT NULL)''')

    def add_to_wishlist(dest):
        pass

    def delete_from_wishlist(dest):
        pass

    def print_wishlist():
        pass