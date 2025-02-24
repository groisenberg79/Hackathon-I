from api_requests import ApiRequest
from wishlist import Wishlist

def user_menu():
    print('\n**** Main Menu ****\n')
    print("1 - Create a new wishlist\n"
          "2 - Show which wishlists are stored\n"
          "3 - Add a destination to wishlist\n"
          "4 - Delete destination from wishlist\n"
          "5 - Delete wishlist\n"
          "0 - Exit the app\n")
    usr_choice = input('Select one of the alternatives above: ').strip()

    if usr_choice not in ['1', '2', '3', '4', '5', '0']:
        print('Invalid choice.')
        user_menu()
    
    elif usr_choice == '0':
        pass

    elif usr_choice == '1':
        wishlist_name = input('Name of the new wishlist (substitute spaces for underscores "_": ').lower()
        Wishlist.create_wishlist(wishlist_name)
        print('New wishlist created.')
        user_menu()
    
    elif usr_choice == '2':
        names = Wishlist.print_names_wishlist()
        if names == "":
            print('No wishlist created yet.')
            user_menu()
        else:
            print('Your lists:\n')
            print(names)
            user_menu()
    
    elif usr_choice == '3':
        pass

    elif usr_choice == '4':
        wishlist_name = input('Name of the wishlist: ').strip().lower()
        table_exists = Wishlist.table_exists(wishlist_name)
        if table_exists:  
            country_name = input('Name of the country: ').strip().lower()
            city_name = input('Name of the city: ').strip().lower()
            row_exists = Wishlist.row_exists(wishlist_name, country_name, city_name)
            if row_exists:
                Wishlist.delete_from_wishlist()
                print('Destination deleted from wishlist.')
                user_menu()
            else:
                print(f'No destination in {city_name}, {country_name} stored in wishlist {wishlist_name}.')
                user_menu()
        else:
            print(f'No wishlist named {wishlist_name} stored.')
            user_menu()

    elif usr_choice == '5':
        wishlist_name = input('Name of the wishlist you wish to delete: ').strip().lower()
        table_exists = Wishlist.table_exists(wishlist_name)
        if table_exists:
            Wishlist.delete_wishlist(wishlist_name)
            print(f'Wishlist {wishlist_name} deleted.')
            user_menu()
        else:
            print(f'No wishlist named {wishlist_name} found.')
            user_menu()
