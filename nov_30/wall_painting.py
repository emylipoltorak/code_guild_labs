import re
import math

def paint_calculator():
    length = []
    height = []
    coats = []
    sq_feet = 0

    start = input('Would you like to paint a wall? y/n: ')
    if start in 'yes':
        length.append(float(input('How long is the wall, in feet? ')))
        height.append(float(input('How high are your ceilings? ')))
        coats.append(float(input('How many coats of paint will you be doing? ')))
    else:
        print('No walls to paint.')

    more_walls = input('Would you like to paint another wall? y/n: ')
    while more_walls in 'yes':
        length.append(float(input('How long is the wall, in feet? ')))
        height.append(float(input('How high are your ceilings? ')))
        coats.append(float(input('How many coats of paint will you be doing? ')))
        more_walls = input('Would you like to paint another wall? y/n: ')

    gallon_cost = float(re.sub('[^0123456789\.]','',input('How much does a gallon of paint cost? ')))

    for index, item in enumerate(length):
        sq_feet += length[index]*height[index]*coats[index]

    gallons = math.ceil(sq_feet/400)
    cost = gallons*gallon_cost

    if gallons > 1:
        return 'You will need {} gallons of paint, which will cost ${:,.2f}'.format(gallons,cost)
    else:
        return 'You will need 1 gallon of paint, which will cost ${:,.2f}'.format(cost)


print(paint_calculator())
