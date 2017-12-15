# Create a Car class with some attributes typical of automobiles, then use it to
# create some instances of different cars.
#
# Create a new directory called cars
# Create the following 2 files inside the cars directory: main.py and car.py
# In car.py, create a class called Car with the following characteristics:
# A shared property called number_of_wheels set to the value 4
# The following instance properties that get set upon initialization:
# color
# number_of_doors
# A honk method that, when called, prints out the word honk
# In main.py, import your Car class and create 2 or 3 instances of cars with different
# characteristics; when you run main.py it should print out the characteristics of your Car instances

class Car:
    def __init__(self, color, number_of_doors):
        self.color = color
        self.number_of_doors = number_of_doors
        self.number_of_wheels = 4

    def honk(self):
        print('HONK!')

if __name__ == '__main__':
    car1 = Car('blue','4')
    print(car1.color)
    car1.honk()
    print(car1.number_of_wheels)
