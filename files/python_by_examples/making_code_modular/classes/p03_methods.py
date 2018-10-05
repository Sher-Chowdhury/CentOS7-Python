# methods are just objects stored inside a class. There are 2 types of methods:
# 1. static  methods
# 2. Instance methods


# https://realpython.com/instance-class-and-static-methods-demystified/

class Car:
    # static method
    def number_of_steering_wheels():
      print("a car has 1 steering wheel")

    # instance method - which uses the 'self' word to reference itself. 
    def wheels(self):
        print('this car has 4 wheels')

# here we call the function without needing to instantiate an object from this class. It's like a library function
Car.number_of_steering_wheels()

# the following won't work, because we have to instantiate an object first. 
# Car.wheels()
# running this would give following error message:

# Traceback (most recent call last):
#  File "p03_cars_class.py", line 21, in <module>
#    Car.wheels()
# TypeError: wheels() missing 1 required positional argument: 'self'

# you call a class in a similar way to how you call a funcition
car_object = Car()

# here we are saying, call the wheels function against the car_object. 
car_object.wheels()



