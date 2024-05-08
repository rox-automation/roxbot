#!/usr/bin/env python3
"""
Mock data generator

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import json
import logging
import math
from typing import Set

import websockets
from roxbot.utils import run_main_async
from websockets.server import serve

log = logging.getLogger("mock")

UPDATE_RATE = 1.0  # Hz
RADIUS = 10.0  # meters
SPEED = 1.0  # meters per second
WS_HOST = "localhost"
WS_PORT = 9001


class MockRobot:
    def __init__(self) -> None:
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.clients: Set[
            websockets.WebSocketServerProtocol
        ] = set()  # This will store active WebSocket connections

    async def sim_loop(self, dt: float = 0.1) -> None:
        """Simulate robot movement."""
        while True:
            self.theta += SPEED * dt / RADIUS
            self.x = RADIUS * (1 - math.cos(self.theta))
            self.y = RADIUS * math.sin(self.theta)
            self.theta %= 2 * math.pi  # Clip theta to 2pi
            await asyncio.sleep(dt)

    async def handler(
        self, websocket: websockets.WebSocketServerProtocol, path: str
    ) -> None:
        """Manage incoming WebSocket connections."""
        self.clients.add(websocket)
        try:
            # Here we could handle incoming messages if needed
            await websocket.wait_closed()
        finally:
            self.clients.remove(websocket)

    async def send_data(self) -> None:
        """Send robot data to all connected UI clients over WebSocket."""
        while True:
            if self.clients:  # Only send data if there are clients connected
                data = {
                    "x": round(self.x, 3),
                    "y": round(self.y, 3),
                    "theta": round(self.theta, 3),
                }
                msg = json.dumps(data)
                await asyncio.gather(*(client.send(msg) for client in self.clients))
                log.info(f"Sending data: {msg}")
            await asyncio.sleep(1.0 / UPDATE_RATE)

    async def main(self) -> None:
        server = await serve(self.handler, WS_HOST, WS_PORT)
        async with server:
            await asyncio.gather(self.sim_loop(), self.send_data())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_main_async(MockRobot().main())
