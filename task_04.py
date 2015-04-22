#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""


import car


class CustomCar(car.Car):
    """Class Custom Car"""

    tires = []

    def __init__(self, color=None, tires=None):
        super(CustomCar, self).__init__(color)
        if tires is None:
            for tires in range(1, 5):
                self.tires.append(CustomTire())
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """Custom Tire Class"""

    __maximum_miles = 500
