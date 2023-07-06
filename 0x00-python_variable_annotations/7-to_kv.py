#!/usr/bin/env python3

"""
Module: 7-to_kv
Contains a type-annotated function `to_kv` that takes a string
and an int/float as arguments and returns a tuple.
The first element of the tuple is the string. The second element
is the square of the int/float as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function: to_kv
    Takes a string and an int/float as arguments and returns a tuple.
    The first element of the tuple is the string.
    The second element is the square of the int/float as a float.
    """
    return k, float(v ** 2)
