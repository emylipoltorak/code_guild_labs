def pretty_print(n, country = 'usa'):
    nanp = ('united states', 'usa', 'american samoa', 'anguilla', 'antigua and barbuda', 'bahamas',
    'barbados', 'bermuda', 'british virgin islands', 'bvi', 'canada', 'cayman islands', 'dominica',
    'dominican republic', 'grenada', 'guam', 'jamaica', 'montserrat', 'northern mariana island',
    'puerto rico', 'saint kitts and nevis', 'saint lucia', 'st vincent and the grenadines', 'sint maarten',
    'trinidad and tobago', 'turks and caicos islands', 'united states virgin islands', 'us virgin islands')
    n = str(n)
    country = country.lower()
    if country in nanp:
        if n[0] == '1':
            print('+{}-{}-{}-{}'.format(n[0],n[1:4],n[4:7],n[7:11]))
        else:
            print('({}){}-{}'.format(n[0:3],n[3:6],n[6:10]))
    elif country in 'denmark':
        print('{} {} {} {}'.format(n[0:2],n[2:4],n[4:6],n[6:8]))
    elif country in 'france':
        if n[0:2] == '33':
            print('+{} {} {} {} {} {}'.format(n[0:2], n[2], n[3:5], n[5:7], n[7:9], n[9:11]))
        else:
            print('{} {} {} {} {}'.format(n[0:2],n[2:4],n[4:6],n[6:8],n[8:10]))
    else:
        print('We don\'t offer formatting services for that country yet.')


def command_line_interface():
    while True:
        n = input('Enter the phone number you would like formatted, or type quit: ')
        if n in 'quitexit':
            print('you have exited the program.')
            exit()
        country = input('What country is the phone number from? ').lower()
        pretty_print(n, country = country)

command_line_interface()
