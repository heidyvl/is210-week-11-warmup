#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module provides functions related to time"""

import time


class Snapshot(object):
    """Object stores Unix Timestamp
    Attribute:
        None
    """

    def __init__(self):
        """ Constructor for Snapshot.
        Arg:
            None
        Attribute:
            created: output for time.time()
        """
        self.created = time.time()
