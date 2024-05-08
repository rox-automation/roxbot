#!/usr/bin/env python3
"""
MQTT bridge for communication between subsystems

This class class abstracts away specific mqtt implementation

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import logging

import orjson
import aiomqtt as mqtt
from pydantic_settings import BaseSettings, SettingsConfigDict

from roxbot.interfaces import MqttMessageProtocol, MqttMessage
from .base import Bridge, JsonSerializableType


class MqttConfig(BaseSettings):
    """MQTT related settings"""

    model_config = SettingsConfigDict(env_prefix="mqtt_")

    host: str = "localhost"
    port: int = 1883


class MqttBridge(Bridge):
    """MQTT bridge for communication between subsystems"""

    def __init__(self, config: MqttConfig | None = None) -> None:
        super().__init__(name="MqttBridge")

        self.config = config or MqttConfig()

        self._client: mqtt.Client | None = None

        self._log = logging.getLogger(self.__class__.__name__)
        self._mqtt_queue: asyncio.Queue[MqttMessageProtocol] = asyncio.Queue(10)

    async def _publish_mqtt(self, client: mqtt.Client) -> None:
        """publish items from mqtt queue.
        an item must have .mqtt_message() and .mqtt_topic() methods"""

        while True:
            item = await self._mqtt_queue.get()
            msg = item.message
            topic = item.topic

            # publish message
            self._log.debug(f"{topic=}, {msg=}")
            await client.publish(topic, msg.encode() if isinstance(msg, str) else msg)
            self._mqtt_queue.task_done()

    async def _receive_mqtt(self, client: mqtt.Client) -> None:
        """receive velocity setpoint from mqtt"""

        self._log.debug("Starting mqtt receive loop")
        async for message in client.messages:
            try:
                cmd = message.payload.decode()  # type: ignore
                self._log.debug(f"{cmd=}")
                self._execute_command(cmd)

            except orjson.JSONDecodeError as e:
                self._log.error(f"Error decoding message {message.payload!r}: {e}")

    def send(self, topic: str, data: JsonSerializableType) -> None:
        """send data to topic"""

        self._mqtt_queue.put_nowait(MqttMessage(topic, data))

    async def subscribe(self, topic: str) -> None:
        """subscribe to topic"""
        if self._client is None:
            raise RuntimeError("MQTT client not initialized")

        self._log.info(f"Subscribing to {topic}")
        await self._client.subscribe(topic)

    async def unsubscribe(self, topic: str) -> None:
        """unsubscribe from topic"""
        if self._client is None:
            raise RuntimeError("MQTT client not initialized")

        self._log.info(f"Unsubscribing from {topic}")
        await self._client.unsubscribe(topic)

    async def main(self) -> None:
        """starting point to handle mqtt communication, starts send and recieve coroutines"""

        self._log.info(f"Connecting to {self.config.host}:{self.config.port}")

        async with mqtt.Client(self.config.host, port=self.config.port) as client:
            self._client = client
            async with asyncio.TaskGroup() as tg:
                tg.create_task(self._receive_mqtt(client))
                tg.create_task(self._publish_mqtt(client))

        self._client = None
