#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Task_03"""

import produce


class Apple(produce.Produce):
    """Subclassing an existing Class"""
    duration = 5356800
    def __init__(self, duration):
        self.duration = duration
        return duration
