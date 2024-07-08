#!/usr/bin/env python3
"""
 Measure the runtime
 """

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ returns total execution time """
    start_time = time.time()
    async.run(wait_n(n, max_delay))
    end_time = time.time()

    total = end_time - start_time
    return total
