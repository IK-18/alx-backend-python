#!/usr/bin/env python3
'''
async_comprehension module
'''
from typing import List


async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension() -> List[float]:
    '''
    Creates a list on numbers
    '''
    return [num async for num in async_generator()]
