#!/usr/bin/env python3
"""
Smoke tests - check basics such as imports etc.

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""


async def dummy_coro() -> None:
    pass


def test_runners() -> None:
    from roxbot.utils import run_main_async

    run_main_async(dummy_coro())
