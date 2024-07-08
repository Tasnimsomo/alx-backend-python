#!/usr/bin/env python3

"""  Let's execute multiple coroutines """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List

async def wait_n(n: int, max_delay: int) -> LIST[float]:
    """ spawn wait_random n times """
    delays = []
    tasks = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
