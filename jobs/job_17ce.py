import asyncio
import websockets
import json
import logging

from datetime import datetime
from concurrent.futures import TimeoutError as ConnectionTimeoutError

from settings import base
from utils.ws import get_ws_url, get_ssl_context
from utils.data import get_send_data, process_data, write_data_to_db


async def task_about_17ce():
    if not (
        base.DB_HOST
        and base.DB_PORT
        # and base.DB_USER
        # and base.DB_PASSWORD
        and base.DB_NAME
    ):
        raise Exception(
            "DB_HOST, DB_POST, DB_USER, DB_PASSWORD and DB_NAME setting must not be empty"
        )

    logging.info("Task is running")
    ws_url = get_ws_url()
    ssl_context = get_ssl_context()

    logging.info("Websock is connecting")
    async with websockets.connect(ws_url, ssl=ssl_context) as websocket:
        send_data = get_send_data()
        await websocket.send(send_data)

        current_time = datetime.now()
        data_list = list()

        while 1:
            try:
                rt = await asyncio.wait_for(websocket.recv(), 300)
            except ConnectionTimeoutError as e:
                logging.error(e)
                logging.info("Data received")
                break
            rt = json.loads(rt)
            if rt.get("type") == "NewData":
                logging.info(rt)
                data = rt.get("data")
                data_list.append(process_data(data, current_time))
    write_data_to_db(data_list)
