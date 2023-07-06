#!/usr/bin/env python3

"""
Module: 9-element_length
Contains a type-annotated function `element_length` that takes a
list as an argument.
The function returns a list of tuples, where each tuple contains
an element from the input list and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function: element_length
    Takes a list as an argument and returns a list of tuples.
    Each tuple contains an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
