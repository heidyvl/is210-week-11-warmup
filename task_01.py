#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""instantiating and accessing custom class instances"""

import produce

TOMATO = produce.Produce()       # no constructor variables/assigned to variable

EGGPLANT = produce.Produce(1311210802)

# Access the attribute of ``TOMATO``save it to a variable

TOMATO_ARRIVAL = TOMATO.arrival

# Call the ``get_expiration()`` method

EGGPLANT_EXPIRES = EGGPLANT.get_expiration()



if __name__ == '__main__':
    print isinstance(TOMATO, produce.Produce)
    print isinstance(EGGPLANT, produce.Produce)
