#!/usr/bin/env python3
""" Asynchronously waits for
    a random delay between 0 and max delay secons."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronously waits for
    a random delay between 0 and max delay secons."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
