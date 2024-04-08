from chapter_05 import *

product_query = \
"""
SELECT
p.product_id,
p.product_name,
p.brand_id,
b.brand_name,
s.sku_id,
pc.product_color_name,
ps.product_size_name
FROM product as p
JOIN sku as s on s.product_id = p.product_id
JOIN product_color as pc on pc.product_color_id = s.product_color_id
JOIN product_size as ps on ps.product_size_id = s.product_size_id
join brand b using (brand_id) 
WHERE p.product_id = 1100
order by pc.product_color_name, ps.product_size_id
"""

async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetch(product_query)
    
@async_timed()
async def query_products_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]

@async_timed()
async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)    

async def main():
    async with asyncpg.create_pool(min_size=4, max_size=7, **DEFAULT_OPTIONS) as pool:
        await query_products_synchronously(pool, 10000)
        await query_products_concurrently(pool, 10000)


asyncio.run(main())