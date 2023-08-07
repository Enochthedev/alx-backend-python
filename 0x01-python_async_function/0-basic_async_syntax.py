#!/usr/bin/env python3
'''
    The basics of async.
'''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds
    and eventually returns the delay.

    Args:
        max_delay (int): The maximum delay value in seconds. Default is 10.

    Returns:
        float: The random delay in seconds.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

# Test cases
print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
