# type: ignore
import pytest
import asyncio
import os

from roxbot import Node

if os.environ.get("CI"):
    pytestmark = pytest.mark.skip(reason="Can't run in CI.")


@pytest.mark.asyncio
async def test_node_instance():
    node = Node()
    asyncio.create_task(node.main())
    await asyncio.sleep(1)
    await node.stop()
