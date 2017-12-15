from car import Car

maggies_car = Car('silver',4)
awful_car = Car('neon yellow', 0)
little_blue_car = Car('blue', 2)

if __name__ == '__main__':
    print(awful_car.number_of_wheels)
    print('This car is awful. It has {} doors!'.format(awful_car.number_of_doors))
    print('Maggie\'s car is {}.'.format(maggies_car.color))
    little_blue_car.honk()
