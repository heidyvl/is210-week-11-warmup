#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclassing an existing class."""

import produce


class Apple(produce.Produce):
    """ A subclass of an existing class to slighty alter its properties.

    Attribute:
        duration(int): An integer.
    """
    duration = 5356800
