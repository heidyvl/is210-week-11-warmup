#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A time module"""

import time


class Snapshot(object):
    """A generic snapshot class.

    Store the time.

    Args:
        created(numeric, optional): The time at snapshot, defaults to
        to the current timestamp.

    Attributes:
        created(numeric): The time at snapshot, in a Unix timestamp.
    """

    def __init__(self, created=None):
        if created is None:
            created = int(time.time())

        self.created = created
