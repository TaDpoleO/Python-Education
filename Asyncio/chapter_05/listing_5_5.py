from chapter_05 import *
from random import sample

def generate_brand_names(words):
    return [(words[index].rstrip(),) for index in sample(range(100), 100)]

async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)

async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(**DEFAULT_OPTIONS)
    await insert_brands(common_words, connection)


asyncio.run(main())