#!/usr/bin/env python3
""" 0. The basics of async """

import asyncio
import random


async def wait_random(max_delay=10):
    """ an asynchronous coroutine that takes in an int arg """
    delay = random.uniform(0, 10)
    await asyncio.sleep(delay)
    return delay
