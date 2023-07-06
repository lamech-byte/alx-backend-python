#!/usr/bin/env python3

"""
Module: 6-sum_mixed_list
Contains a type-annotated function `sum_mixed_list` that takes
a list of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function: sum_mixed_list
    Takes a list of integers and floats as an argument and returns their sum as a float.
    """
    return sum(mxd_lst)
