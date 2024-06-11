#!/usr/bin/env python3
"""Asynchronously generates 10 random numbers
between 0 and 10, one per second."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously generates 10 random numbers
    between 0 and 10, one per second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
