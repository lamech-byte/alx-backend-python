#!/usr/bin/env python3
"""
This module contains a function task_wait_random to create an asyncio.Task.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for wait_random(max_delay).
    Returns the created asyncio.Task object.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
