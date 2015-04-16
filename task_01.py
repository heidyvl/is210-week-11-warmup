#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Import produce and instatiate Objects using produce.Produce"""
import produce

TOMATO = produce.Produce()
EGGPLANT = produce.Produce(arrival=1311210802)
TOMATO_ARRIVAL = TOMATO.arrival
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
