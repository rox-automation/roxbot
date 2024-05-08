#!/usr/bin/env python3
"""
 Example of using the MQTT bridge

 Copyright (c) 2024 ROX Automation - Jev Kuznetsov

 How to use:
 1. Start the MQTT broker with `./start_mosquitto.sh`
 2. Run this script
 3. Run `test_mqtt.sh` to send messages to the broker


"""
from typing import Any
import asyncio
import logging


from roxbot.utils import run_main_async
from roxbot.bridges.mqtt_bridge import MqttBridge

log = logging.getLogger("main")


PUB_TOPIC = "/counter"
SUB_TOPIC = "/test_cmd"


def callback_fcn(args: Any) -> None:
    """example callback function"""
    log.info(f"Running callback with {args=}")


async def send_messages(bridge: MqttBridge) -> None:
    """send test messages to the mqtt broker"""

    counter = 0
    while True:
        msg = f"{counter=}"
        log.info(f"Sending {msg}")

        bridge.send("/test", msg)
        await asyncio.sleep(5)
        counter += 1


async def main() -> None:
    bridge = MqttBridge()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(bridge.main())

        await asyncio.sleep(0.1)  # wait for bridge to connect
        await bridge.subscribe(SUB_TOPIC)

        tg.create_task(send_messages(bridge))


if __name__ == "__main__":
    run_main_async(main())
