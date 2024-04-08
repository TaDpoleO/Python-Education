import requests
import time
from collections import defaultdict

import requests
def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code

url = 'https://www.example.com'


results = defaultdict(int)

time_start = time.time()
for _ in range(100):
    results[get_status_code(url)] += 1
print(results)

time_end = time.time()
print(f'Время выполнения запросов составило: {time_end-time_start:.4f}')