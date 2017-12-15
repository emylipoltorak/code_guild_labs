#variant with filter()

# def greeting():
#     name = input('What is your name? ')
#     age = float(''.join(filter(lambda x: x.isdigit() or x == '.', input('How old are you? '))).rstrip('.'))
#     if age % 1 == 0:
#         age = int(age)
#     greeting = 'Hi there {}! This time next year, you will be {} years old!'.format(name, age+1)
#     stars = '*'*len(greeting)
#     return '\n {} \n {} \n {}'.format(stars, greeting, stars)
#
# print(greeting())

#variant with regex

import re

def greeting():
    name = input('What is your name? ')
    age = float(''.join(re.sub('[^0123456789\.]','',input('How old are you? '))).rstrip('.'))
    if age % 1 == 0:
        age = int(age)
    greeting = 'Hi there {}! This time next year, you will be {} years old!'.format(name, age+1)
    stars = '*'*len(greeting)
    return '\n {} \n {} \n {}'.format(stars, greeting, stars)

print(greeting())
