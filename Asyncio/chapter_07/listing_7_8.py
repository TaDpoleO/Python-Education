import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

counter_lock = Lock()
counter: int = 0

def get_status_code(url: str) -> int:
    global counter
    response = requests.get(url)
    with counter_lock:
        counter = counter + 1
    return response.status_code

async def reporter(request_count: int):
    while counter < request_count:
        print(f'Завершено запросов: {counter}/{request_count}')
        await asyncio.sleep(1)

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        request_count = 200
        urls = ['https://www.example.com' for _ in range(request_count)]
        reporter_task = asyncio.create_task(reporter(request_count))
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]        
        results = await asyncio.gather(*tasks)
        await reporter_task

        res = dict()
        for key in results:
            res[key] = res.get(key, 0)+1
        print(res)

asyncio.run(main())