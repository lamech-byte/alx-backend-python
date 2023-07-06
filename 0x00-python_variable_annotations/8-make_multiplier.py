#!/usr/bin/env python3

"""
Module: 8-make_multiplier
Contains a type-annotated function `make_multiplier` that
takes a float as an argument and returns a function.
The returned function multiplies a float by the given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function: make_multiplier
    Takes a float as an argument and returns a function.
    The returned function multiplies a float by the given multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
