#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some Docstring"""
import car


class CustomCar(car.Car):
    def __init__(self, tires=None):
        if tires == None:
            self.tires = []
            if len(self.tires) <= 4:
                tire1 = CustomTire.tires
                tire2 = CustomTire.tires
                tire3 = CustomTire.tires
                tire4 = CustomTire.tires
                self.tires.append(tire1)
                self.tires.append(tire2)
                self.tires.append(tire3)
                self.tires.append(tire4)
        car.Car.__init__(self)


class CustomTire(car.Tire):
    tires = 1
    _maximum_miles = 500
    
    def __init__(self):
        car.Tire.__init__(self)
        
if __name__ == '__main__':
    mycar = CustomCar()
    print len(mycar.tires)
