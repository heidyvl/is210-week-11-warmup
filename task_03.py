#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A subclass of Produce module."""


import produce


class Apple(produce.Produce):
    """A subclass of imported prodcue class.

    Stores the new duration time, which is different from duration time
    in produce class.

    Attributes:
        duration(numeric): The shelf life of the produce.
    """

    duration = 5356800
