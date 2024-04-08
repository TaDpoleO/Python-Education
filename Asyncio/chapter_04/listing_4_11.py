import asyncio
import aiohttp
from util import async_timed
from chapter_04 import fetch_status
import logging

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = [fetch_status(session, 'https://example.com') for _ in range(3)]
        bad_request = [fetch_status(session, 'python://example.com') for _ in range(2)]
        fetchers = [asyncio.create_task(request) for request in good_request]+[asyncio.create_task(request) for request in bad_request]

        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершенных задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for finished_task in done:
            if finished_task.exception() is None:
                print(await finished_task)
            else:
                logging.error("При выполнении запроса возникло исключение", exc_info=finished_task.exception())

asyncio.run(main())
