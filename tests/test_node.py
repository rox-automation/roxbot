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
    task = asyncio.create_task(node.main())

    # Allow some time for the node to start
    await asyncio.sleep(0.1)

    with pytest.raises(RuntimeError):
        await node.main()

    await asyncio.sleep(1)
    await node.stop()
    await task  # Ensure the main task is awaited to finish cleanly
