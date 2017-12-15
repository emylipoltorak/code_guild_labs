import requests


def get_temp(**kwargs):

    for k, v in kwargs.items():
        payload = {'APPID': '19475ca548deb126b63115788a70c89e', k: v, 'mode': 'json'}
        r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=payload)
        data = r.json()
        description = data['weather'][0]['description']
        temperature = str(round(data['main']['temp'] * 9 / 5 - 459.67, 2))

        print(
            'It is {} degrees fahrenheit in {} right now, with {}.'.format(temperature, payload[k], description))


def interface():
    query = input('Search by (c)ity or (z)ipcode?: ').lower()
    if query in 'city':
        c = input('Enter the name of the city: ').title()
        try:
            print(get_temp(q=c))
        except KeyError:
            print('Invalid Entry')
    elif query in 'zipcode':
        z = int(input('Enter the zipcode: '))
        try:
            print(get_temp(zip=z))
        except KeyError:
            print('Invalid Entry')
    else:
        print('Invalid entry')


if __name__ == '__main__':
    interface()