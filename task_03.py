#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains class Apple, tests for duration of produce."""
import produce


class Apple(produce.Produce):
    """Object child of produce.Produce and checks for duration. 
    Attributes:
        duration (int): Duration of object after arrival.
    """
    duration = 5356800

    def __init__(self):
        """ Duration of Produce. 
        Args:
            duration (int): Duration of produce.

        Returns:
            duration (int): Duration of produce.

        Examples:
            >>> print Apple.duration
            5356800
            >>> print produce.Produce.duration
            604800
        """
        self.duration = duration
        Produce.__init__(self)
