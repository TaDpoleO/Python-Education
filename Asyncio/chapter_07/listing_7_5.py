import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from util import async_timed
from collections import defaultdict

def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code

@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        urls = ['https://www.example.com' for _ in range(1000)]
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        statuses = await asyncio.gather(*tasks)

        results = defaultdict(int)
        for res in statuses:
            results[res] += 1        
        print(results)


asyncio.run(main())