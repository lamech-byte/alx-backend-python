#!/usr/bin/env python3

"""
Module: 5-sum_list
Contains a type-annotated function `sum_list` that takes a list of floats as an argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function: sum_list
    Takes a list of floats as an argument and returns their sum as a float.
    """
    return sum(input_list)
