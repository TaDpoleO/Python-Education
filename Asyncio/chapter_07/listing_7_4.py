import time
import requests
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict

def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code

start = time.time()
with ThreadPoolExecutor() as pool:
    urls = ['https://www.example.com' for _ in range(1000)]
    res = pool.map(get_status_code, urls)

    results = defaultdict(int)
    for status in res:
        results[status] += 1
    print(results)

    end = time.time()
    print(f'Время выполнения запросов составило: {end-start:.4f}')