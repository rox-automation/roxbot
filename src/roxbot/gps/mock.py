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
        self.mqtt_cfg = MqttConfig()
        self.log = logging.getLogger("mock_gps")
        self.current_pose = Pose(0.0, 0.0, 0.0)
        self.mqtt_adapter = MqttAdapter()

    def set_pose(self, args: dict) -> None:
        """example callback function"""
        self.log.info(f"Setting pose to {args=}")

        if not isinstance(args, dict):
            self.log.error("Invalid argument type, must be dict")
            return

        try:
            self.current_pose.x = args["x"]
            self.current_pose.y = args["y"]
            self.current_pose.theta = args["theta"]
        except KeyError as e:
            self.log.error(f"Missing key {e}")

    async def main(self) -> None:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self.mqtt_adapter.main())
            await self.mqtt_adapter.register_callback(SET_POSE_TOPIC, self.set_pose)


if __name__ == "__main__":
    gps = MockGPS()
    run_main_async(gps.main())
