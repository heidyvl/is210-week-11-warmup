#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" creating your own class plus its constructor"""

import time

class Snapshot(object):
    """An object that stores a unix time

    Attributes:
        current (float): Time in seconds.
    """

    def __init__(self):
        """Snapshot class Constructor

        Args:
            created (func): instance attribute assigned the time() function
            using time module.

        Attributes:
            created (func): Instance attribute assigned the time() function
            using time module.
        """

        self.created = time.time()
