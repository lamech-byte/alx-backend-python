#!/usr/bin/env python3
"""
This module contains a function task_wait_n to create an asyncio.Task for
 wait_n.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates an asyncio.Task for wait_n(n, max_delay).
    Returns the list of all the delays (float values) in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
