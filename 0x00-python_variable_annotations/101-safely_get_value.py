#!/usr/bin/env python3
"""
Type annotations for function
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('V')
Value = Union[Any, T]
Default = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Default = None) -> Value:
    if key in dct:
        return dct[key]
    else:
        return default
