#!/usr/bin/env python3
"""
simple listener to receive data from the mock robot

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import logging
from data_generator import WS_HOST, WS_PORT
from websockets.sync.client import connect
from roxbot import LOG_FORMAT
import coloredlogs

log = logging.getLogger("listener")

coloredlogs.install(level=logging.DEBUG, fmt=LOG_FORMAT)


def echo() -> None:
    uri = f"ws://{WS_HOST}:{WS_PORT}"
    with connect(uri) as websocket:
        while True:
            msg = websocket.recv()
            log.info(f"Received: {str(msg)}")  # Decode the bytes before formatting


if __name__ == "__main__":
    try:
        echo()
    except KeyboardInterrupt:
        pass
