import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
from collections import defaultdict

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'

        tasks = [(i+1, asyncio.create_task(fetch_status(session, url))) for i in range(1000)]

        results = defaultdict(int)
        for _, task in tasks:
            status = await task
            results[status] += 1
        print(results)

asyncio.run(main())