import asyncpg
import asyncio
from chapter_05 import *

async def main():
    connection = await asyncpg.connect(**DEFAULT_OPTIONS)
    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():
        cursor = await connection.cursor(query)

        await cursor.forward(800)
        for product in await cursor.fetch(100):
            print(product)

    await connection.close()


asyncio.run(main())