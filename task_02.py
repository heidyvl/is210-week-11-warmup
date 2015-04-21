#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program creates a Unix timestamp."""

import time


class Snapshot(object):
    """A class used to generate a Unix timestamp.

    Attributes:
        None
    """

    def __init__(self):
        """a constructor for Snapshot

        Attributes:
            created:
        """

        self.created = time.time()
