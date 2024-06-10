#!/usr/bin/env python3
"""Asynchronously spawns wait_random coroutines
n times with the specified max_delay."""
import asyncio
from typing import List
from random import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously spawns wait_random
    coroutines n times with the specified max_delay."""
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))
