import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.example.com', 10), 
                    fetch_status(session, 'https://www.example.com', 10), 
                    fetch_status(session, 'https://www.example.com', 1)]
    
        for finished_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                print(await finished_task)
            except TimeoutError:
                print('Произошел тайм-аут!')

asyncio.run(main())