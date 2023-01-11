#!/usr/bin/env python3
""" Coroutine async_generator"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ Generator loops 10 times asyncronously"""

    for i in range(10):
        yield random.random()
        await asyncio.sleep(1)