#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Warmup Task 4"""

import car


class CustomCar(car.Car):
    """Docstring"""

    def __init__(self, color='red', tires=None):
        car.Car.__init__(self)
        self.tires = tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())


class CustomTire(car.Tire):
    """Docstring"""

    __maximum_miles = 500
