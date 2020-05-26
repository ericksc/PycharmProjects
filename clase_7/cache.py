from functools import lru_cache
import time

@lru_cache(maxsize=5000)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
start = time.time()
print([fib(n) for n in range(20000)])
print(fib.cache_info())
print(f'Duration: {time.time() - start}s')
