import asyncio
import aiohttp
from util import async_timed
from chapter_04 import fetch_status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://example.com')) for _ in range(3)]

        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершенных задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for finished_task in done:
            res = await finished_task
            print(res)

asyncio.run(main())
