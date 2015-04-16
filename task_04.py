#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains classes CustomCar and  CustomTire"""
import car


class CustomCar(car.Car):
    """Object child of car.Car and places tires on car.

    Attributes:
        None
    """
    def __init__(self, tires=None):
        """
        Args:
            tires (None): The number of tires on the car.

        Returns:
            tires (list): Each particular tire on the car.

        Examples:
            >>> mycar = CustomCar()
            >>> len(mycar.tires)
            4
            >>> isinstance(mycar.tires[0], CustomTire)
            True
        """
        self.tires = tires
        if (self.tires) == None:
            self.tires = []
            tire = CustomTire()
            if len(self.tires) <= 4:
                self.tires.append(tire)
                self.tires.append(tire)
                self.tires.append(tire)
                self.tires.append(tire)
        else:
            pass
        car.Car.__init__(self)


class CustomTire(car.Tire):
    """Object is child of car.Tire and sets max miles.
    Attributes:
        __maximum_miles (int): Maximum allowed miles per tire.
    """
    __maximum_miles = 500
