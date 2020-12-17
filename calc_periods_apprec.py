#!/bin/python

# A function that calculates the number of periods required to 
# achieve a desired amount of appreciation provided the present
# value, future value, and compounding interest rate as input.

import math

def calc_periods_appreciation(future_value, present_value, interest_rate):
    
    ''' Processing '''
    num_of_periods = math.log(future_value / present_value) / math.log(1 + interest_rate)

    return num_of_periods


''' Method call '''
estimtate_periods = calc_periods_appreciation(200000, 100000, 0.03)

''' Output '''
print(estimtate_periods)