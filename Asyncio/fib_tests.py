import time
import threading
import multiprocessing
import asyncio
from concurrent.futures import ProcessPoolExecutor
from functools import partial

def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print(f'fib({number}) равно {fib(number)}')

def fibs_no_threading(N1, N2):
    print_fib(N1)
    print_fib(N2)
   
def fibs_with_threads(N1, N2):
    fortieth_thread = threading.Thread(target=print_fib, args=(N1,))
    forty_first_thread = threading.Thread(target=print_fib, args=(N2,))
    fortieth_thread.start()
    forty_first_thread.start()
    fortieth_thread.join()
    forty_first_thread.join()
     
def fibs_with_processes(N1, N2):
    fortieth_process = multiprocessing.Process(target=print_fib, args=(N1,))
    forty_first_process = multiprocessing.Process(target=print_fib, args=(N2,))
    fortieth_process.start()
    forty_first_process.start()
    fortieth_process.join()
    forty_first_process.join()

async def fibs_with_asyncio(N1, N2):   
    with ProcessPoolExecutor() as pool:
        loop = asyncio.get_running_loop()
        calls = [partial(print_fib, N1), partial(print_fib, N2)]
        calls_coros = []
        for call in calls:
            calls_coros.append(loop.run_in_executor(pool, call))

        await asyncio.gather(*calls_coros)
  

if __name__ == '__main__':
    # number1 = 40
    # number2 = 41

    number1 = 38
    number2 = 39    

    start = time.time()
    fibs_no_threading(number1, number2)
    end = time.time()
    print(f'Время работы {end - start:.4f} с.\n')

    start_threads = time.time()
    fibs_with_threads(number1, number2)
    end_threads = time.time()
    print(f'Многопоточное вычисление заняло {end_threads - start_threads:.4f} с.\n')    

    start_processes = time.time()
    fibs_with_processes(number1, number2)
    end_processes = time.time()
    print(f'Многопроцессорное вычисление заняло {end_processes - start_processes:.4f} с.\n')

    start_coroutine = time.time()
    asyncio.run(fibs_with_asyncio(number1, number2))    
    end_coroutine = time.time()
    print(f'Асинхронное вычисление заняло {end_coroutine - start_coroutine:.4f} с.')