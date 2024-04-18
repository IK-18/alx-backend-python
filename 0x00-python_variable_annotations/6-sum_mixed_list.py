#!/usr/bin/env python3
'''
Sums a list of integers and floats
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Sums a list of int and float
    '''
    return float(sum(mxd_lst))
