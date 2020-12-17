#!/bin/python

#

import math

def calc_present_value(future_value, interest_rate, n):

    ''' Processing '''
    value = future_value / [(1 + interest_rate) ** n]

    return value

''' Method call '''
pv = calc_present_value(200000, 0.04, 3)


print(pv)
