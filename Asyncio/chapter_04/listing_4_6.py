import asyncio
import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed
from collections import defaultdict

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]        
        
        status_codes = defaultdict(int)
        for status in await asyncio.gather(*requests):
            status_codes[status] += 1
        print(status_codes)

asyncio.run(main())