#!/usr/bin/env python3

"""
Module: 101-safely_get_value
Contains a type-annotated function `safely_get_value` that safely
retrieves a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value
(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Function: safely_get_value
    Takes a dictionary, a key, and an optional default value as
    arguments and returns the value associated with the key.
    If the key is not found in the dictionary, the default value
    is returned.
    """
    if key in dct:
        return dct[key]
    else:
        return default
