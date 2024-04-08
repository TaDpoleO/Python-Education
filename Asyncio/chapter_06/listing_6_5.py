import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from chapter_06 import *

def count(count_to: int) -> int:
    counter = 0
    while counter < count_to:
        counter = counter + 1
    return counter

@async_timed()
async def main():
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [1, 3, 5, 22, 100000000]

        calls = [partial(count, num) for num in nums]
        call_coros = [loop.run_in_executor(process_pool, call) for call in calls]

        results = await asyncio.gather(*call_coros)
        for result in results:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())