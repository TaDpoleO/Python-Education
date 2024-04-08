from chapter_04 import *

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'
        tasks = [asyncio.create_task(fetch_status(session, url, i)) for i in range(4)]

        done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED, timeout=3)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')
        
        for done_task in done:
            print(await done_task)

        for undone_task in pending:
            undone_task.cancel()

asyncio.run(main())