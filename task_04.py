#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Warmup Task 4"""

import car


class CustomCar(car.Car):
    """A customized automobile"""

    def __init__(self, color='red', tires=None):
        """Constructor for CustomCar() class.

        Args:
            color (string): Color of the car, defaults to 'red'.
            tires (list): A list of CustomTire() objects. Defaults to None.

        Attributes:
            car.Car (class): Calls the Car() class.
            tires (list): CustomTire objects to determine miles on Tires.
        """
        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())


class CustomTire(car.Tire):
    """A customized rubber donut-shaped object

    Args:
       miles (int): Number of miles on the Tire.

    Attributes:
        miles (int): Number of miles on the Tire.
    """

    __maximum_miles = 500
