#!/usr/bin/env python3
""" Let's execute multiple coroutines
    at the same time with async
"""
import bisect
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays in ascending order"""
    list_of_delays: List[float] = []
    for _ in range(n):
        x = asyncio.create_task(wait_random(max_delay))
        bisect.insort(list_of_delays, await x)
    return list_of_delays
