#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program ."""

import car


class CustomCar(car.Car):
    """car.Car is parent class for CustomCar

    Args:
        None
    """
    def __init__(self, tires=None):
        """Constructor for CustomCar

        Args:
            tires(int): Number of tires.
        Attribute:
            tires(int): Number of tires.
        Returns:
            Returns a list of tires.
        Examples:
            >>> mycar = CustomCar()
            >>>len(mycar.tire)
            4
            >>>isinstance(mycar.tires[0], CustomTire)
        """

        self.tires = tires
        car.Car.__init__(self, tires)
        self.tires = tires
        tires = CustomTire()
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(tires)


class CustomTire(car.Tire):
    """car.Tire is parent class for CustomTire
    Arg:
        None
    """

    __maximum_miles = 500
