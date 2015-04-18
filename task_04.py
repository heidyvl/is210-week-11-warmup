#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A new car module."""

import car


class CustomTire(car.Tire):
    """A Tire class.

    Stores the miles and maxium_miles of tire.

    Args:
        miles(numeric, optional): the miles of tire used. Defaults to 0.

    Attributes:
        miles(numeric): the miles of tire used.
        maxium_miles(numeric): the maxium_miles of tire used.
    """
    __maximum_miles = 500

    def __init__(self, miles=0):
        car.Tire.__init__(self, miles=0)

    def get_maxium_miles(self):
        """Returns the maxiu_miles of tire.

        Returns:
            intger: 500.

        Example:

        >>> mytire = CustomTire()
        >>> mytire.get_maxium_miles()
        500
        """
        return self.__maxium_miles


class CustomCar(car.Car):
    """ A CustomCar class.

    Stores the color of car and four instances of the CustomTire() class.

    Args:
        color(str): a string of color.
        tires(list): a list of four instances of the CustomTire() class.
    """
    def __init__(self, color=None, tires=None):
        self.tires = tires
        car.Car.__init__(self, color)
        if tires is None:
            tires = [CustomTire(), CustomTire(), CustomTire(), CustomTire()]
