#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some Docstring"""

import time

class Snapshot(object):
    """ Creates a Snapshot of time.time() and returns value.
    """
    
    def __init__(self):
        self.created = time.time()
