import asyncio
import asyncpg
import logging
from chapter_05 import *

async def main():
    connection = await asyncpg.connect(**DEFAULT_OPTIONS)

    try:
        async with connection.transaction():
            bad_insert = "INSERT INTO brand VALUES(9999, 'big_brand')"
            await connection.execute(bad_insert)
            await connection.execute(bad_insert)
    except Exception:
        logging.exception('Ошибка при выполнении транзакции')
    finally:
        query = "SELECT brand_name FROM brand WHERE brand_name LIKE 'big_%'"
        brands = await connection.fetch(query)
    
        for brand in brands:
            print(brand)

        await connection.close()

if __name__ == '__main__':
    asyncio.run(main())