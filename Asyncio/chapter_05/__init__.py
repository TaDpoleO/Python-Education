import asyncpg
import asyncio
from util import *

DEFAULT_OPTIONS = dict(host='127.0.0.1', port=5432, user='postgres', database='products', password='password')

class AsyncpgConnection():
    def __init__(self, *args, **kwargs) -> None:
        self._connection = None
        self._args = args
        self._kwargs = kwargs

    async def __aenter__(self):
        self._connection = await asyncpg.connect(*self._args, **self._kwargs)
        return self._connection
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._connection.close()

def load_common_words():
    with open('./chapter_05/common_words.txt') as file:
        words = []
        for word in file:
            words.append(word.rstrip())
        return words
        