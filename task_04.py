#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some Docstring"""
import car
import pprint

class CustomCar(car.Car):
    
    def __init__(self,color,tires=None):
        self.tires = tires
        if self.tires == None:
            self.tires = []
            tire = CustomTire()
            if len(self.tires) <= 4:
                self.tires.append(tire)
                self.tires.append(tire)
                self.tires.append(tire)
                self.tires.append(tire)
        else:
            pass
        car.Car.__init__(self, color)


class CustomTire(car.Tire):

    __maximum_miles = 500
    


if __name__ == '__main__':
    mycar = CustomCar('blue')
    print len(mycar.tires)
