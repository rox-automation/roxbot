#!/usr/bin/env python3
"""
Node example.

There is no need to create a base Node class, a more flexible approach is to
use adapters to add functionality to a class.

In this example, we don't even need to create a Node class, we can just use a couple
of coros.

When only one instance of a node is required, it is simpler to use coroutines in a module.

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import logging

from roxbot.adapters import MqttAdapter, MqttLogger
from roxbot.utils import run_main_async

log = logging.getLogger("main")
log.setLevel(logging.DEBUG)


def listener(args: list | dict) -> None:
    """example callback function"""
    log.info(f"Running callback with {args=}")


async def talker() -> None:
    counter = 0

    while True:
        log.debug(f"debug message {counter=}")
        log.info(f"info message {counter=}")
        counter += 1
        await asyncio.sleep(1)


async def main() -> None:
    mqtt_adapter = MqttAdapter()

    mqtt_logger = MqttLogger(log)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(mqtt_adapter.main())
        await mqtt_adapter.register_callback("/test_cmd", listener)

        tg.create_task(mqtt_logger.main())
        tg.create_task(talker())


if __name__ == "__main__":
    run_main_async(main())
