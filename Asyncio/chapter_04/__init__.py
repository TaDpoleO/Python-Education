import asyncio
import aiohttp
from util import async_timed

async def fetch_status(session: aiohttp.ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status