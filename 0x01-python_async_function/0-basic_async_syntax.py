#!/usr/bin/env python3
"""This is hthe basics of asynchronous"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    This takes an int argument and wait for
    random delay and returns delay time
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
