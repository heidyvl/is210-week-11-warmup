#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" subclassing an existing class to slightly alter its properties"""

import produce

class Apple(produce.Produce):
    """ A subclass of an existing class, slighty alter properties.

    Attribute:
        duration(int): An integer.

    Examples:
        >>> print Apple.duration
        5356800

        >>> print produce.Produce.duration
        604800
    """

    duration = 5356800   # Altering value of a class attribute



if __name__ == '__main__':
    print Apple.duration
    print produce.Produce.duration
