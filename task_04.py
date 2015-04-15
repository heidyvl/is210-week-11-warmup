#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some Docstring"""

import car

class CustomCar(car.Car):
    
    def __init__(self):
        car.Car.__init__(self)
        
        
class CustomTire(car.Tire):
    pass

if __name__ == '__main__':
    mycar = CustomCar()
    # len(mycar.tires)
