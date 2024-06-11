#!/usr/bin/env python3
"""
Gps mock for testing

Functionality:
---------------

* publish gps position and orientation

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

from dataclasses import dataclass
import logging
import asyncio
from roxbot.adapters import MqttAdapter
from roxbot.config import MqttConfig
from roxbot.utils import run_main_async


SET_POSE_TOPIC = "/mock_gps/set_pose"


@dataclass
class Pose:
    x: float
    y: float
    theta: float


class MockGPS:
    def __init__(self) -> None:
        self.pose = Pose(0.0, 0.0, 0.0)

        self._mqtt_cfg = MqttConfig()
        self._log = logging.getLogger("mock_gps")

        self._mqtt_adapter = MqttAdapter()

    def set_pose(self, args: dict) -> None:
        """example callback function"""
        self._log.info(f"Setting pose to {args=}")

        if not isinstance(args, dict):
            self._log.error("Invalid argument type, must be dict")
            return

        try:
            self.pose.x = args["x"]
            self.pose.y = args["y"]
            self.pose.theta = args["theta"]
        except KeyError as e:
            self._log.error(f"Missing key {e}")

    async def main(self) -> None:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self._mqtt_adapter.main())
            await self._mqtt_adapter.register_callback(SET_POSE_TOPIC, self.set_pose)


if __name__ == "__main__":
    gps = MockGPS()
    run_main_async(gps.main())
