#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK11 warmup task 02 - build a new class."""

import time


class Snapshot(object):
    """Returns current Unix timestamp."""

    def __init__(self):
        """Constructor for the Snapshot() class.

        Attributes:
           created (float): The Unix timestamp.
        """

        created = time.time()
        self.created = created
