#!/usr/bin/env python3
"""
This module contains an async_comprehension coroutine that collects 10 random
 numbers.
"""

from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over
      async_generator.
    Returns the list of 10 random numbers.
    """
    return [i async for i in async_generator()]
