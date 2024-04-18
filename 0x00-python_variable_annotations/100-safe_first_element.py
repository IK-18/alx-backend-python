#!/usr/bin/env python3
'''
Safely retrieves the first element of a list
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Retrieves the first element of a list if it exists
    '''
    if lst:
        return lst[0]
    else:
        return None
