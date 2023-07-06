#!/usr/bin/env python3

"""
Module: 102-type_checking
Contains a type-annotated function `zoom_array` that
zooms an array by repeating its elements.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """
    Function: zoom_array
    Zooms an array by repeating its elements.

    Args:
        lst (Tuple[int]): The input array as a tuple.
        factor (int): The zoom factor, indicating how many times
        each element should be repeated.

    Returns:
        List[int]: The zoomed array as a list.

    Examples:
        >>> zoom_array((1, 2, 3), 3)
        [1, 1, 1, 2, 2, 2, 3, 3, 3]
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
