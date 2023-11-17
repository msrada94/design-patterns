# Classification: creation
# Defines interface for creating an object
# Lets subclasses decide which object
# DDefers instantiation to subclasses
# Also known as Virtual Constructor


# SIMPLE FACTORY PATTERN STRUCTURE:
import abc
import creational.factory.car
from creational.factory.volvo_car import VolvoCar
from creational.factory.tesla_car import TeslaCar
from creational.factory.jaguar_car import JaguarCar


class CarFactory:
    cars = {}

    def __init__(self):
        self.load_cars()

    def load_cars(self):
        for clazz in creational.factory.car.Car.get_subclasses():
            self.cars.update({clazz.__name__: clazz})

    def create_instance(self, car_name):
        if car_name in self.cars:
            return self.cars[car_name]
        else:
            raise ValueError("Invalid car name")


if __name__ == '__main__':
    print(CarFactory().create_instance('VolvoCar'))
