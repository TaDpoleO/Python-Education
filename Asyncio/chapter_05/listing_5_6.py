from chapter_05 import *
from random import randint, sample

def gen_products(common_words, brand_id_start: int, brand_id_end: int, products_to_create):
    products = []
    for _ in range(products_to_create):
        description = [common_words[index] for index in sample(range(1000), 10)]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((" ".join(description), brand_id))
    return products

def gen_skus(product_id_start: int, product_id_end: int, skus_to_create: int):
    skus = []
    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))
    return skus

async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(**DEFAULT_OPTIONS)
    
    product_tuples = gen_products(common_words, brand_id_start=105, brand_id_end=204, products_to_create=1000)
    await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)", product_tuples)
    
    sku_tuples = gen_skus(product_id_start=1001, product_id_end=2000, skus_to_create=100000)
    await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)", sku_tuples)

    await connection.close()


asyncio.run(main())