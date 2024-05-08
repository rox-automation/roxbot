#!/usr/bin/env python3
"""
MQTT bridge for communication between subsystems

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

from typing import Callable
from roxbot.interfaces import JsonSerializableType


class MqttBridge:
    """MQTT bridge for communication between subsystems"""

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def send(self, topic: str, msg: JsonSerializableType) -> None:
        """send a message to a topic"""
        pass

    def register_callback(self, topic: str, callback: Callable) -> None:
        """register a callback for a topic"""
        pass
