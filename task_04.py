#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" subclassing, demonstrate *has-a* and *is-a* concepts.
    inside the ``car`` module as we'll be
    extending the ``Car()`` class found inside."""

import car


class CustomCar(car.Car):
    """Subclass of class car

    Args:
        None
    """

    def __init__(self, tires=None):
        """Constructor for subclass CustomCar().

        Args:
            tires(int): input arg for car tires (tires=new instance attribute)

        Attribute:
            tires(int):no of car tires

        Returns:
            returns a list of car tires to four instances

        Examples:
            >>> MYCAR = CustomCar()
            >>>len(MYCAR.tire)
            4

            >>>isinstance(mycar.tires[0], CustomTire)
            True
        """

        self.tires = tires

        car.Car.__init__(self, tires) # new instance attribute
        self.tires = tires            # default = None
        tires = CustomTire()
        if self.tires is None:        # for none empty
            self.tires = []
            while len(self.tires) < 4:  # appending list for 4 instances
                self.tires.append(tires)

class CustomTire(car.Tire):
    """Subclass of class car, Parent class for CustomTire.

    Arg:
        car.tire(car): attribute of the car

    Attribute:
        __maximum_miles(int): maximum miles for tire
    """
    __maximum_miles = 500     # private now




if __name__ == '__main__':
    MYCAR = CustomCar()
    print len(MYCAR.tires)
    print isinstance(MYCAR.tires[0], CustomTire)
