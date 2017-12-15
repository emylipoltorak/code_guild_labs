import json
def lat_long(city):
    with open('data.json', 'r') as f:
        data = json.load(f)
        latitude = data[city]['Position']['Latitude']
        longitude = data[city]['Position']['Longitude']
        return 'The Latitude/Longitude of {} is {}/{}.'.format(city,latitude,longitude)

if __name__ == '__main__':
    print(lat_long('Portland'))
