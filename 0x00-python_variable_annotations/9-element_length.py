#!/usr/bin/env python3
"""
Returns a list of lengths of lists
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of lengths of lists
    """
    return [(i, len(i)) for i in lst]
