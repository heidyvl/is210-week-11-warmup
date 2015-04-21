#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK11 warmup task 04."""


import car


class CustomCar(car.Car):
    """A customized version of the Car class."""

    def __init__(self, color='red', tires=None):
        """Constructor for the CustomCar() class.

        Args:
            color (string): The color of the car. Defaults to 'red'.
            tires (int): The amount of tires. Defaults to None.

        Attributes:
            color (string): The color of the car.
            tires (int): The amount of tires.

        Examples:
            >>> mycar = CustomCar()
            >>> len(mycar.tires)
            4
            >>> isinstance(mycar.tires[0], CustomTire)
            True
        """
        car.Car.__init__(self, color)
        self.color = color
        self.tires = tires
        tire = CustomTire()
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(tire)


class CustomTire(car.Tire):
    """Constructor for the CustomTire() class.

    Args:
        None.

    Attributes:
        maximum_miles (int): A pseudo-private indicator of the max miles.
    """
    __maximum_miles = 500
