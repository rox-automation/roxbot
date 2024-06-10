#!/usr/bin/env python3
"""
simple MQTT logger, forwards log messages to an MQTT topic


Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import aiomqtt as mqtt

from logging import LogRecord, Formatter
from logging.handlers import QueueHandler


class MqttLogger:
    """MQTT bridge for communication between subsystems"""

    def __init__(
        self, broker: str = "localhost", port: int = 1883, log_topic: str = "/log"
    ) -> None:
        self._broker = broker
        self._port = port
        self._log_topic = log_topic
        self._mqtt_queue: asyncio.Queue[LogRecord] = asyncio.Queue(10)

    def get_log_handler(self) -> QueueHandler:
        """return a logging handler that logs to mqtt"""
        handler = QueueHandler(self._mqtt_queue)
        return handler

    async def _publish_mqtt(self) -> None:
        """publish items from mqtt queue."""

        formatter = Formatter(
            fmt="%(asctime)s.%(msecs)03d [%(name)s] %(levelname)s %(message)s",
            datefmt="%H:%M:%S",
        )

        async with mqtt.Client(self._broker, port=self._port) as client:
            while True:
                log_record = await self._mqtt_queue.get()
                log_msg = formatter.format(log_record)

                # publish message
                await client.publish(self._log_topic, log_msg.encode())
                self._mqtt_queue.task_done()

    async def main(self) -> None:
        """starting point to handle mqtt communication, starts send and recieve coroutines"""

        await self._publish_mqtt()
