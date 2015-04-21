#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclassing to demonstrate the has-a and is-a concepts."""

import car


class CustomCar(car.Car):
    """Demonstrating the has-a and is-a concepts.
    """
    def __init__(self, tires=None):
        """Constructor for CustomCar class.

        Args:
            tires(default is None): an argument
        Attributes:
            self.tires = an emplty list to append.
        """
        car.Car.__init__(self)
        if tires is None:
            self.tires = []
            self.tires.append(CustomTire())
            self.tires.append(CustomTire())
            self.tires.append(CustomTire())
            self.tires.append(CustomTire())
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """A simple docstring.
    """
    __maximum_miles = 500
