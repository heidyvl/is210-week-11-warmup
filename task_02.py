#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week11 task_02 module"""


import time


class Snapshot(object):
    """contructor of snapshot that returns the current Unix Timestamp

    attributes:
        none
    """

    def __init__(self):
        """a constructor for Snapshot

        args:
            time(mix): the timestamp of unix system
        attributes:
            time(mix): the timestamp of unix system
        """

        self.created = time.time()
