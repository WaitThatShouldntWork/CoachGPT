import asyncio
import json
import logging
from fastapi import WebSocket
from typing import Callable
from .types import Handlers, MessageTypes

logger = logging.getLogger(__name__)

heartbeat_timeout = 30
pong = json.dumps({"type": MessageTypes.PONG.value})


def create_on_ping():
    heartbeat_timer: asyncio.Task | None = None

    async def heartbeat(disconnect: Callable, ws: WebSocket):
        try:
            await asyncio.sleep(heartbeat_timeout)
            await disconnect(ws)
        except asyncio.CancelledError:
            pass

    def on_ping(websocket: WebSocket, disconnect: Callable, data: str | None):
        nonlocal heartbeat_timer

        asyncio.create_task(websocket.send_json(pong))

        if heartbeat_timer is not None:
            heartbeat_timer.cancel()

        heartbeat_timer = asyncio.create_task(heartbeat(disconnect, websocket))

    return on_ping


def on_chat(websocket: WebSocket, disconnect: Callable, data: str | None):
    logger.info(f"Chat message: {data}")


handlers: Handlers = {MessageTypes.PING: create_on_ping(), MessageTypes.CHAT: on_chat}
