import time
from multiprocessing import Pool

def say_hello(name: str, delay: int = 0) -> str:
    time.sleep(delay)
    return f'Привет, {name}'

def main():
    with Pool() as process_pool:
        hi_jeff = process_pool.apply_async(say_hello, args=('Jeff', 1))
        hi_john = process_pool.apply_async(say_hello, args=('John', 10))
        print(hi_jeff.get())
        print(hi_john.get())

if __name__ == "__main__":
    time_start = time.time()
    main()
    time_end = time.time()
    print(f'Программа завершилась за {time_end-time_start} с.')