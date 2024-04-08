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
        urls[10] = 'python://example.com'
        urls[900] = 'python://example.com'
        requests = [fetch_status(session, url) for url in urls]                  

        results = await asyncio.gather(*requests, return_exceptions=True)

        status_codes = defaultdict(int)
        errors = []

        for res in results:
            if isinstance(res, Exception):
                errors.append(res)
            else:
                status_codes[res] += 1
        
        print(status_codes)
        print(errors)

asyncio.run(main())