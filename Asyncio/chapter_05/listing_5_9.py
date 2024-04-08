import asyncio
import asyncpg
from chapter_05 import *

async def main():
    connection = await asyncpg.connect(**DEFAULT_OPTIONS)
    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_2')")

    query = "SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"
    brands = await connection.fetch(query)
    
    for brand in brands:
        print(brand)

    await connection.close()

if __name__ == '__main__':
    asyncio.run(main())