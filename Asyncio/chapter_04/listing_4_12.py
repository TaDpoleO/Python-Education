import asyncio
import aiohttp
from chapter_04 import fetch_status
from util import async_timed

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://example.com', 3)), 
                    asyncio.create_task(fetch_status(session, 'https://bad_site.com')), 
                    asyncio.create_task(fetch_status(session, 'https://example.com', 10))]
        
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                print(f'При выполнении запроса возникло исключение: {done_task.exception()}')

        for pending_task in pending:
            pending_task.cancel()


asyncio.run(main())