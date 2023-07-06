#!/usr/bin/env python3

"""
Module: 100-safe_first_element
Contains a duck-typed function `safe_first_element` that safely
retrieves the first element from a sequence.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function: safe_first_element
    Takes a sequence as an argument and returns the first element if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
