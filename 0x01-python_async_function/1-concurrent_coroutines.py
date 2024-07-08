#!/usr/bin/env python3

"""  Let's execute multiple coroutines """

import asyncio
import wait_random from ./0-basic_async_syntax
from typing import List

async def wait_n(n: int, max_delay: int) -> LIST[float]:
    """ spawn wait_random n times """
    delays = []

    for i in range(n):
        wait_random(max_delays) += delays
        results = await asyncio.gather(*delays)
        return results
