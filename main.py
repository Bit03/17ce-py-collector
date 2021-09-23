import os
import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from jobs.job_17ce import task_about_17ce

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S",
        filename=f"{os.getcwd()}/monitor.log",
        filemode="w",
    )
    scheduler = AsyncIOScheduler()
    scheduler.add_job(task_about_17ce, "interval", minutes=1)

    scheduler.start()
    asyncio.get_event_loop().run_forever()
