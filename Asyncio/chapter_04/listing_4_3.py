import asyncio
import aiohttp
from aiohttp import ClientSession

async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=1)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status
    
async def main():
    session_timeout = aiohttp.ClientTimeout(total=3, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        result = await fetch_status(session, 'https://example.com')
        print(result)

asyncio.run(main())