#!/usr/bin/env python3
"""
Creates a multiplier from a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier from a float
    """
    return lambda x: x * multiplier
