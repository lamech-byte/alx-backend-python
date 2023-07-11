#!/usr/bin/env python3
"""
This module contains a measure_runtime coroutine that executes
 async_comprehension multiple times in parallel.
"""

import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime by executing async_comprehension four times in
      parallel.
    Returns the total runtime.
    """
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
