from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import geocoder
import pandas as pd


def get_location(user_address=None):
    if user_address:
        geolocator = Nominatim(scheme='http')
        location = geolocator.geocode(user_address)
        return location.latitude, location.longitude
    else:
        location = geocoder.ip('me')
        return location.latlng


def get_data():
    data = pd.read_csv('p_a.csv')
    data = data.dropna(subset=['lat', 'lng'])
    return data


def find_nearby(user_loc, distance):
    data = get_data()
    art_list = []
    count = 0
    for index, row in data.iterrows():
        art_loc = (row['lat'], row['lng'])
        miles_away = round(vincenty(art_loc, user_loc).miles, 1)
        if miles_away <= distance:
            art_list.append('{} by {} can be found at {}, {} miles.'.format(row['title'],
                                                                            row['artist'], row['location'], miles_away))
            count += 1
    print('{} works of public art found within {} miles.'.format(count, distance))
    return '\n'.join(art_list)


def interface():
    while True:
        u_address = input('What is your address? Include the city, or enter x to use your current location: ')
        if u_address == 'x':
            u_address = get_location()
        else:
            u_address = get_location(u_address)
        dist = float(input('How far are you willing to travel? '))
        print(find_nearby(u_address, dist))
        cont = input('Would you like to search again? Y/N: ').lower()
        if cont == 'n':
            break


if __name__ == '__main__':
    interface()
