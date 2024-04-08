import asyncio
from asyncio.subprocess import Process

async def main():
    program = ['python', './chapter_13/listing_13_9.py']
    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE, stdin=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate(b'Zoot')
    print(stdout.decode(encoding='utf-8'))
    print(stderr)


asyncio.run(main())