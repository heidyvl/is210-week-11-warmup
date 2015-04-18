#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Warmup Task 2"""

import time


class Snapshot(object):
    """An object that stores a snapshot of time

    Attributes:
        current (float): Time in seconds since the Epoch as a float.
    """

    def __init__(self, created=time.time()):
        """Constructor for Snapshot class.

        Args:
            created (func): instance attribute assigned the time() function
            of the time module.

        Attributes:
            created (func): Instance attribute assigned the time() function
            of the time module.
        """
        self.created = created
