#!/usr/bin/env python3
"""module 1"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n"""
    list1 = []
    for x in range(n):
        list1.append(await wait_random(max_delay))
    return sorted(list1)
