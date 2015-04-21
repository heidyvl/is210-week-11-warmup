#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 11 task_04"""


import car


class CustomCar(car.Car):
    """ object that store properties of custom car

    args:
        car.Car: properties of Car
    attributes:
        None
    """

    def __init__(self, tires=None):
        """constructor of CustomCar class

        args:
            tires(int): number of tires used on the car

        attributes:
            tires(int): number of tires used on the car

        return:
            tires(lists): number of tires on the car

        exampls:
            >>> mycar = CustomCar()
            >>> len(mycar.tires)
            4

        """
        car.Car.__init__(self)
        self.tires = tires
        tire = CustomTire(tires)

        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(tire)


class CustomTire(car.Tire):

    """object of car of customTire

    args:
        car.tire(car): property of car
    attributes:
         __maximum_miles(int): maximum miles on each tire
    """

    __maximum_miles = 500
