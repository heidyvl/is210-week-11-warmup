#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Warmup Task 3"""

import produce


class Apple(produce.Produce):
    """Object that stores data from produce module.

    Attributes:
        produce.Produce(class): Stores the arrival time and estimated shelf-life
        of the produce.

    Args:
        arrival (numeric, optional): The time the produce arrived. Defaults to
        the current timestamp.
    """

    duration = 5356800
