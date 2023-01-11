#!/usr/bin/env python3
""" async_comprehension """

from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """10 rand nums using comprehension """

    return [i async for i in async_generator()]