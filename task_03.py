#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK11 warmup task 03 - using subclasses."""

import produce


class Apple(produce.Produce):
    """A subclass of produce.

    Attributes:
        duration (int): The lenght until expiration.
    """

    duration = 5356800
