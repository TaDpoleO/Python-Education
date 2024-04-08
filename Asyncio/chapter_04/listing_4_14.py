from chapter_04 import *

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'
        pending = [asyncio.create_task(fetch_status(session, url, 2)) for i in range(100)]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f'Число завершившихся задач: {len(done)}')
            print(f'Число ожидающих задач: {len(pending)}')
            
            for done_task in done:
                print(await done_task)     

asyncio.run(main())