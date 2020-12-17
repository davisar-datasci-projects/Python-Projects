#!/bin/python

# A function that calculates the periodic interest rate required to
# achieve a desired amount of appreciation provided the present
# value, future value, and n number of years as input.

import math

def calc_periodic_interest(future_value, present_value, n):

    ''' Processing '''
    interest_rate = (future_value / present_value)**(1 / n) - 1

    return interest_rate

''' Method call '''
calculate_interest = calc_periodic_interest(200000, 100000, 9)

''' Output '''
print(calculate_interest)