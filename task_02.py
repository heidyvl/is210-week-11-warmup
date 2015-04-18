#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a class from ground-up."""

import time


class Snapshot(object):
    """A class docstring.

    Attributes:
        created: the output if time.time()
    """
    def __init__(self):
        self.created = time.time()
