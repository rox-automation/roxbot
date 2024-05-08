#!/usr/bin/env python3
"""
MQTT bridge for communication between subsystems

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

from .base import Bridge, JsonSerializableType


class MqttBridge(Bridge):
    """MQTT bridge for communication between subsystems"""

    def __init__(self, host: str, port: int) -> None:
        super().__init__(name="MqttBridge")
        self.host = host
        self.port = port

    def send(self, topic: str, data: JsonSerializableType) -> None:
        pass

    async def serve(self) -> None:
        pass
