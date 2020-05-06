#!/usr/bin/env python3
"""Async Generator"""
import random
import asyncio
from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ The coroutine will collect 10 random numbers
        using an async comprehensing over async_generator
        and return them
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
