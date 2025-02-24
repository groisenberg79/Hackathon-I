from api_requests import ApiRequest
from wishlist import Wishlist

def user_menu():
    print('\n**** Main Menu ****\n')
    print("1 - Create a new wishlist\n"
          "2 - Show which wishlists are stored\n"
          "3 - Print a wishlist\n"
          "4 - Add a destination to wishlist\n"
          "5 - Delete destination from wishlist\n"
          "6 - Delete wishlist\n"
          "0 - Exit the app\n")
    usr_choice = input('Select one of the alternatives above: ').strip()

    if usr_choice not in ['1', '2', '3', '4', '5', '6', '0']:
        print('\nInvalid choice.')
        user_menu()
    
    elif usr_choice == '0':
        pass

    elif usr_choice == '1':
        wishlist_name = input('Name of the new wishlist (substitute spaces for underscores "_"): ').lower()
        Wishlist.create_wishlist(wishlist_name)
        print('\nNew wishlist created.')
        user_menu()
    
    elif usr_choice == '2':
        names = Wishlist.print_names_wishlist()
        if names == "":
            print('\nNo wishlist created yet.')
            user_menu()
        else:
            print('\n* Your lists:\n')
            print(names)
            user_menu()

    elif usr_choice == '3':
        wishlist_name = input('Which wishlist would you wish to see? ').strip().lower()
        table_exists = Wishlist.table_exists(wishlist_name)
        if table_exists:
            wishlist = Wishlist.print_wishlist(wishlist_name)
            if wishlist == 0:
                print(f'\nNo places added yet to {wishlist_name}.')
                user_menu()
            else:
                print(wishlist)
            user_menu()
    
    elif usr_choice == '4':
        place = list()
        wishlist_name = input('Name of the wishlist: ').strip().lower()
        exists = Wishlist.table_exists(wishlist_name)
        if not exists:
            print(f'\nNo wishlist named {wishlist_name} found.')
            user_menu()
        else: 
            country_name = input('Name of the country you are interested in: ').strip().lower()
            country_code = ApiRequest.request_loc_code(country_name)
            if country_code == 0:
                print('\nInvalid country name.')
                user_menu()
            else:
                place.append(country_name)
                city_name = input('Name of the city you are interested in: ').strip().lower()
                lat_lon = ApiRequest.request_loc(city_name, country_code)
                if lat_lon == 0:
                    print('\nInvalid city, country pair.')
                    user_menu()
                else:
                    place.append(city_name)
                    temp_hum = ApiRequest.request_temp_hum(lat_lon[0], lat_lon[1])
                    place.append(temp_hum[0])
                    place.append(temp_hum[1])
                    print(f"Average temp. in {city_name}: {temp_hum[0]}; Humidity in {city_name}: {temp_hum[1]}%.\n")
                    while True:
                        usr_choice = input("Would you like to add this destination to the wishlist (y/n)? ").strip().lower()
                        if usr_choice not in ['y', 'n']:
                            print('\nInvalid choice.')
                            pass
                        else:
                            break
                    if usr_choice == 'n':
                        user_menu()
                    else:
                        Wishlist.add_to_wishlist(wishlist_name,place)
                        print('\nDestination added to wishlist.')
                        user_menu()

    elif usr_choice == '5':
        wishlist_name = input('Name of the wishlist: ').strip().lower()
        table_exists = Wishlist.table_exists(wishlist_name)
        if table_exists:  
            country_name = input('Name of the country: ').strip().lower()
            city_name = input('Name of the city: ').strip().lower()
            row_exists = Wishlist.row_exists(wishlist_name, country_name, city_name)
            if row_exists:
                Wishlist.delete_from_wishlist(wishlist_name, country_name, city_name)
                print('\nDestination deleted from wishlist.')
                user_menu()
            else:
                print(f'\nNo destination in {city_name}, {country_name} stored in wishlist {wishlist_name}.')
                user_menu()
        else:
            print(f'\nNo wishlist named {wishlist_name} stored.')
            user_menu()

    elif usr_choice == '6':
        wishlist_name = input('Name of the wishlist you wish to delete: ').strip().lower()
        table_exists = Wishlist.table_exists(wishlist_name)
        if table_exists:
            Wishlist.delete_wishlist(wishlist_name)
            print(f'\nWishlist {wishlist_name} deleted.')
            user_menu()
        else:
            print(f'\nNo wishlist named {wishlist_name} found.')
            user_menu()

def main():
    print('Welcome to the Travel Wishlist Builder!')
    user_menu()

main()
