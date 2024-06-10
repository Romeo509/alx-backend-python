#!/usr/bin/env python3
"""Asynchronously spawns task_wait_random n
    times with the specified max_delay."""

import asyncio
from typing import List
from asyncio import Task

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously spawns task_wait_random n
    times with the specified max_delay."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

# For testing
if __name__ == "__main__":
    import asyncio

    async def test(n: int, max_delay: int) -> None:
        print(await task_wait_n(n, max_delay))

    n = 5
    max_delay = 6
    asyncio.run(test(n, max_delay))
