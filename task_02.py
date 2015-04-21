#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains class Snapshot, returns Unixtimestamp."""
import time


class Snapshot(object):
    """ Creates a Snapshot of time.time() and returns value.
    Attributes:
        None
    """
    def __init__(self):
        """Takes Snapshot of the time and returns Unixtimestamp.
        Args:
            created (float): Time in Unixtimestamp
        Returns:
            created (float): Time in Unixtimestamp
        Examples:
            >>> newtime = Snapshot()
            >>> newtime.created
            1429211380.193029
        """
        self.created = time.time()
